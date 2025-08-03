import fitz  # PyMuPDF
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import io


class PDFSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vertical PDF Splitter")

        self.canvas = Canvas(root, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)

        self.open_button = Button(root, text="Open PDF", command=self.load_pdf)
        self.open_button.pack(side=LEFT)

        self.save_button = Button(root, text="Save Split PDF", command=self.save_pdf, state=DISABLED)
        self.save_button.pack(side=RIGHT)

        self.direction_var = StringVar(value="left")
        self.left_first = Radiobutton(root, text="Left first", variable=self.direction_var, value="left")
        self.right_first = Radiobutton(root, text="Right first", variable=self.direction_var, value="right")
        self.left_first.pack(side=LEFT)
        self.right_first.pack(side=LEFT)

        self.canvas.bind("<B1-Motion>", self.drag_split_line)
        self.canvas.bind("<Button-1>", self.set_split_line)

        self.pdf_path = None
        self.doc = None
        self.first_page_img = None
        self.split_x = None
        self.scale = 1

    def load_pdf(self):
        path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if not path:
            return
        self.pdf_path = path
        self.doc = fitz.open(self.pdf_path)
        page = self.doc.load_page(0)
        pix = page.get_pixmap()
        self.image_width = pix.width
        self.image_height = pix.height
        self.split_x = self.image_width // 2

        img = Image.open(io.BytesIO(pix.tobytes("ppm")))
        self.first_page_img = img
        self.display_image()
        self.save_button.config(state=NORMAL)

    def display_image(self):
        self.tk_img = ImageTk.PhotoImage(self.first_page_img)
        self.canvas.delete("all")
        self.canvas.config(width=self.tk_img.width(), height=self.tk_img.height())
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)
        if self.split_x:
            self.canvas.create_line(self.split_x, 0, self.split_x, self.tk_img.height(), fill="red", width=2)

    def set_split_line(self, event):
        self.split_x = event.x
        self.display_image()

    def drag_split_line(self, event):
        self.set_split_line(event)

    def save_pdf(self):
        if not self.doc or self.split_x is None:
            messagebox.showerror("Error", "No PDF loaded or no split line defined.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF Files", "*.pdf")])
        if not save_path:
            return

        output = fitz.open()

        for i in range(len(self.doc)):
            page = self.doc.load_page(i)
            width, height = page.rect.width, page.rect.height
            split_px = self.split_x
            split_pt = split_px * width / self.image_width

            # Define split rectangles in PDF units
            left_rect = fitz.Rect(0, 0, split_pt, height)
            right_rect = fitz.Rect(split_pt, 0, width, height)

            # Choose order based on user input
            rects = [left_rect, right_rect] if self.direction_var.get() == "left" else [right_rect, left_rect]

            for rect in rects:
                # Create a new page with the same dimensions as the clipped region
                new_page = output.new_page(width=rect.width, height=rect.height)
                # Copy content from source page using clipping rectangle
                new_page.show_pdf_page(new_page.rect, self.doc, i, clip=rect)

        output.save(save_path)
        output.close()
        messagebox.showinfo("Done", "PDF saved successfully!")

if __name__ == "__main__":
    root = Tk()
    app = PDFSplitterApp(root)
    root.mainloop()

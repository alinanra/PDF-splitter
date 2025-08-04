# 🪓 PDF Splitter: Vertical Page Split Based on First Page

This is a lightweight Python desktop application that allows users to split all pages in a PDF file **vertically**, based on where the user drags a line on the **first page preview**.

Each page is split into two new pages, maintaining original resolution and layout. The user can choose whether the **left** or **right** side should come first.

---

## ✨ Features

- 📄 Preview the first page and set a vertical split position with a draggable red line.
- 🔀 Choose whether the left or right side becomes the first page.
- 📚 Applies the same vertical split to **all pages** in the PDF.
- 🧱 Saves a new PDF with **double the pages** — each original page split into two.
- 🖋️ Preserves vector quality, text, and resolution — not just images.
- 🖥️ Cross-platform desktop GUI built with Tkinter.

---

## 🧰 Requirements

- Python 3.7 or higher  
- `PyMuPDF` (`pymupdf`)  
- `Pillow`  

Install dependencies with:

```bash
pip install pymupdf pillow
```

## 🖼️ Screenshots

### Step 1: Set the vertical split line  
Drag the red line to where you want to split all pages:

![Step 1 – Vertical split line](<img width="763" height="668" alt="image" src="https://github.com/user-attachments/assets/a605c37e-50d2-4bd4-98b0-b556c1a8cc5f" />
)

---

### Step 2: Choose page order and save  
Select whether the left or right side is first, then click save:

![Step 2 – Save split PDF](<img width="765" height="670" alt="image" src="https://github.com/user-attachments/assets/5a474375-8edf-4f89-a654-a747b567b5aa" />
)

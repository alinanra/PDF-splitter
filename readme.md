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

![Step 1 – Vertical split line](https://github.com/user-attachments/assets/f2dd97b6-3033-4fbe-b27c-4cd12e008e6f)

---

### Step 2: Choose page order and save  
Select whether the left or right side is first, then click save:

![Step 2 – Save split PDF](https://github.com/user-attachments/assets/09362988-22ca-43b6-88a2-76278c271b2e)

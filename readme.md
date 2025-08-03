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

Drag the red line
![Preview of vertical split line](https://github.com/user-attachments/assets/f2dd97b6-3033-4fbe-b27c-4cd12e008e6f)

Choose whether the right or left page comes first and click save to choose where to save.

![Save split PDF prompt](https://github.com/user-attachments/assets/f5ba8d11-ecae-4cc4-aa76-c5b57af08291)


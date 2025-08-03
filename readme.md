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

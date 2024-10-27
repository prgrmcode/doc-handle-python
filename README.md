# PDF Table of Contents Inserter

This Python project consists of scripts to read a table of contents (TOC) from a text file, insert it into a PDF document, and make the TOC entries clickable, linking to the correct pages in the document. The project uses the PyMuPDF library for PDF manipulation.

## Features

- Extracts a table of contents from a text file or directly from a PDF.
- Inserts the table of contents into the beginning of a PDF document.
- Creates clickable links for each TOC entry that navigate to the correct page in the document.
- Handles multi-page TOC by adding additional pages as needed.
- Adjusts page numbers in the TOC entries to account for the added TOC pages.

## Requirements

- Python 3.x
- PyMuPDF (also known as fitz)

## Installation

1. Install Python 3.x if you haven't already.
2. Install the PyMuPDF library using pip:

```bash
pip install pymupdf
```

## Usage

### Extracting TOC from PDF

Use the pdf-handle-toc.py script to extract the table of contents from a PDF file and write it to a text file.

### Inserting TOC into PDF

Use the pdf-insert-toc.py script to read the table of contents from the text file and insert it into the PDF, making the entries clickable.

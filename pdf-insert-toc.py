import fitz  # PyMuPDF
import re

def read_toc_from_file(toc_file):
    toc = []
    with open(toc_file, "r") as f:
        for line in f:
            match = re.match(r'(Article\s+\d+)\t([^\t]+)\tp\.\s*(\d+)', line)
            if match:
                article_number, article_name, page_num = match.groups()
                toc.append((article_number, article_name, int(page_num)))
    return toc


def insert_table_of_contents(pdf_path, toc, output_pdf_path):
    document = fitz.open(pdf_path)
    toc_pages = []
    y_offset = 72  # Start after the title
    max_y_offset = 792 - 72  # Page height minus margin

    # Create the first TOC page
    toc_page = document.new_page(0)
    toc_pages.append(toc_page)
    toc_page.insert_text((72, y_offset), "Table of Contents\n\n", fontsize=12)
    y_offset += 24  # Move to the next line after the title

    for article_number, article_name, page_num in toc:
        if y_offset > max_y_offset:
            # Create a new TOC page if the current one is full
            toc_page = document.new_page(len(toc_pages))
            toc_pages.append(toc_page)
            y_offset = 72  # Reset y_offset for the new page

        link_text = f"{article_number}\t{article_name}\tp. {page_num}"
        toc_page.insert_text((72, y_offset), link_text, fontsize=12)
        toc_page.insert_link({
            "kind": fitz.LINK_GOTO,
            "from": fitz.Rect(72, y_offset - 12, 500, y_offset + 2),
            "page": page_num + len(toc_pages) - 1,  # Adjust page number for added TOC pages
            "zoom": 0
        })
        y_offset += 14  # Move to the next line

    # Adjust the page numbers in the TOC entries
    for i, (article_number, article_name, page_num) in enumerate(toc):
        toc[i] = (article_number, article_name, page_num + len(toc_pages))

    # Save the modified PDF
    document.save(output_pdf_path)


# Path to your PDF file
pdf_path = "./EECC.pdf"
output_pdf_path = "./EECC_with_TOC.pdf"
toc_file = "table_of_contents.txt"

# Read table of contents from the text file
toc = read_toc_from_file(toc_file)

# Insert table of contents into the PDF and make them clickable
insert_table_of_contents(pdf_path, toc, output_pdf_path)

print(f"Table of contents has been inserted into the PDF and saved as {output_pdf_path}")
import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    print(f"pages_count: {len(document)}")
    text = ""
    page_texts = []
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        page_text = page.get_text()
        text += page_text
        page_texts.append((page_num + 1, page_text))  # Store page number and text
    return text, page_texts

# def generate_table_of_contents(page_texts):
#     toc = []
#     # Refined regular expression to match article headings (e.g., "Article 24\nConsultation of interested parties")
#     pattern = re.compile(r'(Article\s+\d+)\n([A-Z][a-zA-Z\s\-]+)')
#     for page_num, page_text in page_texts:
#         matches = pattern.findall(page_text)
#         for match in matches:
#             article_number, article_name = match
#             # Ensure that only the article name is captured
#             article_name = article_name.split('\n')[0].strip()
#             toc.append((article_number, article_name, page_num))
#     return toc


def generate_table_of_contents(page_texts):
    toc = []
    # Refined regular expression to match article headings (e.g., "Article 24\nConsultation of interested parties")
    pattern = re.compile(r'^(Article\s+\d+)\n([A-Z][a-zA-Z\s,\-]+)(?=\n[A-Z]|$)', re.MULTILINE)
    for page_num, page_text in page_texts:
        matches = pattern.findall(page_text)
        for match in matches:
            article_number, article_name = match
            # Ensure that only the article name is captured
            article_name = article_name.split('\n')[0].strip()
            # Additional check to ensure the article name is not part of a sentence
            if not re.search(r'\.\s*$', article_name):
                toc.append((article_number, article_name, page_num))
    return toc


# Path to your PDF file
pdf_path = "./EECC.pdf"

# Extract text from PDF
text, page_texts = extract_text_from_pdf(pdf_path)

# Generate table of contents
toc = generate_table_of_contents(page_texts)  
    
# Write table of contents to a file
output_file = "table_of_contents.txt"
with open(output_file, "w") as f:
    for article_number, article_name, page_num in toc:
        f.write(f"{article_number}\t{article_name}\tp. {page_num}\n\n")

print(f"Table of contents has been written to {output_file}")
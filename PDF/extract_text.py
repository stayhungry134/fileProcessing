"""
name: extract_text
create_time: 2023/8/28 17:19
author: Ethan

Description: 从 PDF中提取文字
"""
import PyPDF2
from my_self.openai总结 import summarize_text


def extract_text_from_pdf(pdf_path, page_start=1, page_end=1):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        for page_number in range(page_start - 1, page_end - 1 if page_end else num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()

    return text


pdf_path = 'D:/Downloads/深入浅出Vue.js (刘博文) (Z-Library).pdf'

text = extract_text_from_pdf(pdf_path, 86, 93)

print(summarize_text(text))




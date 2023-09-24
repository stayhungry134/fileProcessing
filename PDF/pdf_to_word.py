"""
File Name: pdf_to_word
Author: Ethan
date: 12/6/2021
Description: 使用 Python 将 PDF 文件转换为 Word 文件
"""
import PyPDF2

file_path = 'E:/Document/PDF/张怀—前端简历.pdf'

with open(file_path, 'r', encoding='utf-8') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    print(page.extractText())

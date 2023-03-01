"""
name: ocr_pdf.py
create_time: 2023-02-06
author: Ethan White

Description: 将扫描版 PDF 文件转换为可以复制文本的 PDF 文件
需要安装 Tesseract https://digi.bib.uni-mannheim.de/tesseract/，下载安装后添加环境变量
需要安装 Ghostscript https://ghostscript.com/releases/gsdnld.html
"""
import ocrmypdf

file_path = "F:/OneDrive/learning materials/books/Program/现代操作系统  原书第4版.pdf"
out_path = "E:/现代操作系统(第4版)"
ocrmypdf.ocr(file_path, out_path, deskew=True, skip_text=True)

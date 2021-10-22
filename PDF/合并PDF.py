"""
File Name: 合并PDF
Author: Ethan
date: 10/19/2021

Description: 用于处理PDF 的合并
"""

# 导入相关库
import os
from PyPDF2 import PdfFileMerger

# 文件所在路径
dir_path = 'F:/Document/PDF/彩印/'

# 获取文件名
pdf_list = [f for f in os.listdir(dir_path)]

# 拼接文件夹和文件名，获取文件路径列表
pdfs = [os.path.join(dir_path, filename) for filename in pdf_list]

# 创建 PDF 合并对象
pdf_merger = PdfFileMerger()
for pdf in pdfs:
    # 合并 PDF 文件
    pdf_merger.append(pdf)

# 保存文件
pdf_merger.write('F:/Document/PDF/彩印.pdf')
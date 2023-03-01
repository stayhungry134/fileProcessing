import csv
import pdfkit

# with open('../files/learn_word.csv', 'r') as csv_file:
#     reader = csv.reader(csv_file)
#     # for i in reader:
#     #     print(i)
#     with open('word.html', 'a', encoding='utf-8') as html:
#         for i in reader:
#             html.write('<li><span>{}</span><span>{}</span></li>'.format(i[0], i[1]))
#         html.write('</ul></body></html>')



# HTML文件生成PDF
def html_to_pdf(html, to_file):
    # 将 wkhtmltopdf.exe 程序绝对路径传入 config 对象
    # 对应的软件需要下载安装 https://wkhtmltopdf.org/downloads.html
    path_wkhtmltopdf = 'F:/Tools/wkhtmltopdf/bin/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    # 生成PDF文件，to_file为文件路径
    pdfkit.from_file(html, to_file, configuration=config)
    print("完成")


html_to_pdf('word.html', 'demo.pdf')
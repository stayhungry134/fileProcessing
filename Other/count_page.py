"""
name: count_page.py
create_time: 2023-03-01
author: Ethan White

Description: 
"""

page_dic = {f'{i}': 0 for i in range(10)}


def counter_num(page_str):
    """统计数据出现次数，page为页码（字符串）"""
    for item in page_str:
        page_dic[item] += 1


with open('../0_files/123.txt', 'r', encoding='utf-8') as f:
    pages = f.readlines()
    for page in pages:
        counter_num(page)

print(page_dic)


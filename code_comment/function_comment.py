"""
name: function_comment.py
create_time：2022-08-09
author: Ethan

Description：用于处理 Python 文件，然后通过注释生成对应的文档
"""
import re

def handle_py():
    with open('../.files/orderutils.py', encoding='utf-8') as f:
        # 匹配函数及其下面的注释(单引号或双引号)
        res = re.findall(r'def \w*[^)]*\):\s*[\'\'\'|\"\"\"]+[^\'\'\'|^\"\"\"\"]*', f.read())
        with open('../.files/api.md', 'w+', encoding='utf-8') as m:
            for api in res:
                m.writelines(api.replace('def ', '\n').replace("\n", '').replace(" ", "").replace("'''", "("))
                m.write('\n')

def generate_document():
    with open('../.files/api.md', encoding='utf-8') as md:
        with open('../.files/xmall_API.md', 'a+', encoding='utf-8') as xmall:
            for line in md.readlines():
                ls = line.replace("):", "").replace('\n', '').split("(")
                # xmall.writelines("1. `{}`，=={}==，{}\n".format(ls[0], ls[1], ls[2]))
                xmall.writelines("| `{}` | {} | {} |\n".format(ls[0], ls[1], ls[2]))


generate_document()


# s = 'def handel(targer, evenrt, data):\n"""我是一个参数"""\n\ndef handle(targer, evenrt, data):\n"""我是一个参数"""\n\n'
#
# res = re.findall(r'def \w*[^)]*\):\s*[\'\'\'|\"\"\"]*[^\'\'\'|^\"\"\"\"]*', s)
# print(res)
#
# s = "handle_when_new_order(order:Order):(新订单处理"
# ls = s.replace("):", "").split("(")
# print("1. `{}`，=={}==，{}\n".format(ls[0], ls[1], ls[2]))

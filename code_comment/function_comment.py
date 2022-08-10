"""
name: function_comment.py
create_time：2022-08-09
author: Ethan

Description：用于处理 Python 文件，然后通过注释生成对应的文档
"""
import re
import os


class FunctionComment():
    def __init__(self, file_path, project_name):
        self.files = None
        self.file_path = file_path
        self.project_name = project_name

    def walk_folder(self):
        """
        遍历出项目中的文件（浅遍历）
        :return:
        """
        # 判断项目名称是否为文件夹
        self.file_path = os.path.join(self.file_path, self.project_name)
        if os.path.isdir(self.file_path):
            # self.files = [file for file in os.walk(project_path)][0][2]
            self.files = list(os.walk(self.file_path))[0][2]
            print(self.files)
        else:
            self.files = list(self.project_name)

    def handle_py(self):
        """
        整理函数和注释，并将其存入一个中转文件当中
        :return:
        """
        for file in self.files:
            with open('{}/{}'.format(self.file_path, file), encoding='utf-8') as f:
                # 匹配函数及其下面的注释(单引号或双引号)
                res = re.findall(r'def \w*[^)]*\):\s*[\'\'\'|\"\"\"]+[^\'\'\'|^\"\"\"\"]*', f.read())
                with open('{}/med.md'.format(file_path), 'a+', encoding='utf-8') as m:
                    print(file)
                    m.write("## {}\n".format(file.split("_")[0]))
                    for api in res:
                        m.writelines(api.replace('def ', '\n').replace("\n", '').replace(" ", "").replace("'''", "(").replace('"""', '('))
                        m.write('\n')
                    m.write("\n---\n")

    def generate_document(self):
        """
        生成文档 markdown 格式
        :return:
        """
        with open('{}/med.md'.format(file_path), encoding='utf-8') as md:
            with open('{}/{}.md'.format(file_path, self.project_name), 'a+', encoding='utf-8') as api_file:
                for line in md.readlines():
                    if line[:2] == "##":
                        api_file.writelines(line)
                    else:
                        try:
                            ls = line.replace("):", "").replace('\n', '').split("(")
                            # xmall.writelines("1. `{}`，=={}==，{}\n".format(ls[0], ls[1], ls[2]))
                            api_file.writelines("| `{}` | {} | {} |\n".format(ls[0], ls[1], ls[2]))
                        except:
                            pass

    def main(self):
        self.walk_folder()
        self.handle_py()
        self.generate_document()


file_path = '../.files'
project_name = 'xmall'

fun = FunctionComment(file_path, project_name)
# fun.walk_folder()
fun.main()



# s = 'def handel(targer, evenrt, data):\n"""我是一个参数"""\n\ndef handle(targer, evenrt, data):\n"""我是一个参数"""\n\n'
#
# res = re.findall(r'def \w*[^)]*\):\s*[\'\'\'|\"\"\"]*[^\'\'\'|^\"\"\"\"]*', s)
# print(res)
#
# s = "handle_when_new_order(order:Order):(新订单处理"
# ls = s.replace("):", "").split("(")
# print("1. `{}`，=={}==，{}\n".format(ls[0], ls[1], ls[2]))

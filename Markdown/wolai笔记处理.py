import os

# 我来笔记保存的文件夹（记得在后面加 / ）
# E:\study\编程\前端开发\JavaScript\JavaScript基础\开始学习
dirpath = 'E:/study/编程/前端开发/JavaScript/DOM/'

# 读取文件夹下面的内容
files = os.listdir(dirpath)


# 判断是否是文件夹
# def if_dir(filepath):
#     if os.path.isdir(filepath):
#         os.chdir(dirpath)
#     else:
#         return filepath


# 遍历更改我来笔记的内容
for file in files:
    if file[-2:] == 'md':
        filepath = dirpath + file
        with open(filepath, 'r', encoding='utf-8') as f:
            new_file = f.read().replace('&ensp;', '')
            with open(filepath, 'w', encoding='utf-8') as f1:
                f1.write(new_file)
    else:
        pass
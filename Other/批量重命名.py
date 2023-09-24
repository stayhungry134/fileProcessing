import os

# 文件夹路径
file_path = 'E:/image/netbian/meinv/'

# 获取所有文件，存入列表
file_list = os.listdir(file_path)


for index, file in enumerate(file_list):
    # 设置旧文件名（路径 + 文件名）
    oldername = file_path + file
    # 设置新文件名
    newname = f'{file_path}image_{index + 1}.jpg'

    # 重命名
    os.rename(oldername, newname)

    print(oldername, '-------->', newname)


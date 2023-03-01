import os

# 文件夹路径
file_path = 'E:/image/壁纸/'

# 获取所有文件，存入列表
file = os.listdir(file_path)

n = 0

for i in file:
    # 设置就文件名（路径 + 文件名）
    oldername = file_path + file[n]
    # 设置新文件名
    newname = file_path + 'image_' + str(n+1) + '.jpg'

    # 重命名
    os.rename(oldername, newname)

    print(oldername, '-------->', newname)

    n += 1

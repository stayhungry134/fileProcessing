"""
File Name: 处理手机壁纸
Author: Ethan
date: 10/19/2021

Description: 判断宽度是否大于高度，如果大于，就删除
"""
import os
from PIL import Image

# 文件夹路径
file_path = 'E:/images/phone/Wallpaper_1.jpg'

# 获取所有文件，存入列表
# file = os.listdir(file_path)

wallpaper = Image.open(file_path)

print(wallpaper.size)
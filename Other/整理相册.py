"""
File Name: 整理相册
Author: Ethan
date: 10/20/2021

Description:  通过相册的文件名整理相册到相应文件夹
"""

import os


# 初始文件夹
src_path = 'F:/OneDrive/PersonalFiles/相机/'

# 目标文件夹
dst_path = 'F:/OneDrive/PersonalFiles/个人相册/相机/'

# 相册列表
img_list = os.listdir(src_path)
# 筛选出相机图片，存于一个列表中
camera_img = [img for img in img_list if img[:3] == 'IMG']
# aims_camera_img = list(map(lambda img: img[:3] + '_' + img[3:11] + '_' + img[11:], camera_img))

# 文件夹目录
dir_list = list(set(map(lambda img: img[4:10], camera_img)))


# 整理相册
def order_img():
    # 每个月的图片
    for dir in dir_list:
        images = [img for img in camera_img if img[4:10] == dir]
        # 创建目录
        aims_path = dst_path + dir[:4] + '年' + dir[4:] + '月'
        if not os.path.exists(aims_path):
            os.mkdir(aims_path)
        else:
            pass

        for image in images:
            # print(src_path + image + '----->' + aims_path + '/' + image[:3] + '_' + image[3:11] + '_' + image[11:])
            # print(src_path + image + '----->' + aims_path + '/' + image)
            try:
                os.rename(src_path + image, aims_path + '/' + image)
                print(src_path + image + '----->' + aims_path + '/' + image)
            except FileExistsError:
                # 如果文件已存在，则删除原文件
                os.remove(src_path + image)
order_img()
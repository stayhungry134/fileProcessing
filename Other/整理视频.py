# coding=utf8
"""
File Name: 整理视频
Author: Ethan
date: 12/16/2021

Description:  通过视频的文件名整理视频到相应文件夹
"""

import os


# 初始文件夹
src_path = 'F:/个人文件/视频/'

# 目标文件夹
dst_path = 'F:/个人文件/个人视频/'

# 相册列表
video_list = os.listdir(src_path)
# 筛选出相机图片，存于一个列表中
camera_video = [video for video in video_list if video[:3] == 'VID']
# aims_camera_video = list(map(lambda video: video[:3] + '_' + video[3:11] + '_' + video[11:], camera_video))

# 文件夹目录
dir_list = list(set(map(lambda video: video[4:10], camera_video)))


# 整理视频
def order_video():
    # 每个月的视频
    for dir in dir_list:
        videos = [video for video in camera_video if video[4:10] == dir]
        # 创建目录
        aims_path = dst_path + dir[:4] + dir[4:]
        if not os.path.exists(aims_path):
            os.mkdir(aims_path)
        else:
            pass

        for video in videos:
            # print(src_path + video + '----->' + aims_path + '/' + video[:3] + '_' + video[3:11] + '_' + video[11:])
            # print(src_path + video + '----->' + aims_path + '/' + video)
            try:
                os.rename(src_path + video, aims_path + '/' + video)
                print(src_path + video + '----->' + aims_path + '/' + video)
            except:
                pass
order_video()
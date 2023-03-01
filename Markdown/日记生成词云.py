"""
name: 日记生成词云.py
create_time: 2022-09-28
author: Ethan

Description: 
"""
import os
import numpy as np
from PIL import Image
import jieba
from wordcloud import WordCloud


dirpath = "F:/2021/"
words = []
stopwords = [i.strip() for i in open('../files/hit_stopwords.txt', encoding='utf-8').readlines()]


def get_text(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        text = f.read().split('今日日记')[1]
        dairy_words = jieba.lcut(text)
        dairy_words = [word for word in dairy_words
                       if word not in stopwords and len(word) > 1]
        return dairy_words


filepaths = os.listdir(dirpath)
for file in filepaths:
    if file[-2:] == 'md':
        filepath = dirpath + file
        print(filepath)
        try:
            dairy_words = get_text(filepath)
            words = [*words, *dairy_words]
        except:
            continue



# 生成词云
wc = WordCloud(background_color="white",  # 设置背景颜色
               max_words=500,  # 最大显示词数
               max_font_size=100,  # 最大字体
               # min_font_size=50,
               # width=2000,
               # height=3000,
               mask=np.array(Image.open('../files/heart.jpg')),  # 选择背景图片
               font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体
               )

wc.generate(' '.join(words))
wc.to_file('1.png')
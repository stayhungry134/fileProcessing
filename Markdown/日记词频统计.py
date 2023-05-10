"""
name: 日记词频统计.py
create_time: 2022-09-28
author: Ethan

Description: 用于统计日记的词语频率
"""
import jieba
import os

dirpath = "F:/2021/"
count = {}
words = []

def get_text(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        text = f.read().split('今日日记')[1]
        text = jieba.lcut(text)
        return text


def counter_text(words):
    for word in words:
        if len(word) == 1:
            continue
        else:
            count[word] = count.get(word, 0) + 1


filepaths = os.listdir(dirpath)
for file in filepaths:
    if file[-2:] == 'md':
        filepath = dirpath + file
        print(filepath)
        try:
            text = get_text(filepath)
            words = [*words, *text]
            counter_text(text)
        except:
            continue


items = list(count.items())
items.sort(key=lambda x: x[1], reverse=True)
with open('../0_files/dairywords.txt', 'w+', encoding='utf-8') as f:
    for i in range(100):
        word, count = items[i]
        f.writelines("{:<5} --> {:>6}\n".format(word, count))
        # print("{:<5} --> {:>6}".format(word, count))
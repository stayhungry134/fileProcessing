import wordcloud
from imageio import imread
import jieba

mask = imread("E:/download/img/chinaMap.png")

filepath = "../../file/text/2019政府工作报告.txt"
t = open(filepath, "rt", encoding="utf-8").read()
report = (jieba.lcut(t))
ls = " ".join(report)

w = wordcloud.WordCloud(height=700, width=1000, font_path="msyh.ttc", background_color="white", mask=mask)
w.generate(ls)

w.to_file("../../file/img/2019report.png")

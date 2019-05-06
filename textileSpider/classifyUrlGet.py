# -*- coding:utf-8 -*-

from requests_html import HTMLSession
import csv

session = HTMLSession()
url = 'http://www.31ml.com/baike/'
op = open('classify_title.csv', 'w', encoding="utf-8")
writer = csv.writer(op)  # 使用w的方式打开，
# 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。


def get_print():
    site = session.get(url)
    #  查看页面内容
    classifys = site.html.find('.bk_nrjj dt h2 a')  # 使用CSS选择器选择内容
    for classify in classifys:
        print('爬虫得到内容如下')
        classify_title = classify.text
        url_link = classify.absolute_links
        print(classify_title)  # 获取分类标题
        print(classify.absolute_links)  # 获取分类链接
        save2csc(classify_title, url_link)


def save2csc(classify_title, url_link):
    # header = ['classify_title', 'url']
    # writer.writerow(header)
    csvrow = []
    csvrow.append(classify_title)
    csvrow.append(url_link)
    writer.writerow(csvrow)


if __name__ == '__main__':
    print("开始处理")
    get_print()
    print("处理结束")
    op.close()

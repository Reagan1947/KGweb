# -*- coding:utf-8 -*-

from requests_html import HTMLSession
import csv
import numpy as np
import re

session = HTMLSession()
op = open('2_index.csv', 'w', encoding='utf-8')
writer = csv.writer(op)  # 使用w的方式打开，
# 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。


def get_url_in_file():
    index_2_link = []
    index_2_title = []
    with open('classify_title.csv', encoding='utf-8') as csvfile_1:
        writer = csv.reader(csvfile_1)
        for row in writer:
            if np.shape(row) == (2,):
                res = re.findall(r'\{\'(.*?)\'\}', row[1])
                index_2_link.append(res[0])
                index_2_title.append(row[0])
    # 对link列表进行转置
    tran_link = np.transpose(index_2_link)
    tran_titl = np.transpose(index_2_title)
    for i in range(np.shape(tran_link)[0]):
        # print(tran_titl[i], tran_link[i])
        get_page_content(tran_titl[i], tran_link[i])


def get_page_content(tran_titl, tran_link):
    site = session.get(tran_link)
    #  查看页面内容
    classifys = site.html.find('.blue')  # 使用CSS选择器选择内容
    for classify in classifys:
        print('爬虫得到内容如下')
        classify_title = classify.text
        url_link = classify.absolute_links
        print(classify_title)  # 获取分类标题
        print(classify.absolute_links)  # 获取分类链接
        save2csc(tran_titl, classify_title, url_link)

def save2csc(tran_titl, classify_title, url_link):
    # header = ['classify_title', 'url']
    # writer.writerow(header)
    csvrow = []
    csvrow.append(tran_titl)
    csvrow.append(classify_title)
    csvrow.append(url_link)
    writer.writerow(csvrow)

if __name__ == '__main__':
    get_url_in_file()
    print("处理结束")
    op.close()

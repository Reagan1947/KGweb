# -*- coding:utf-8 -*-

from requests_html import HTMLSession
import csv
import numpy as np
import re
import sys
import io

session = HTMLSession()
op = open('3_index.csv', 'a', encoding='utf-8')
writer = csv.writer(op)  # 使用w的方式打开，
# 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # Change default encoding to utf8

def get_url_in_file():
    index_3_link = []
    index_3_title_1 = []
    index_3_title_2 = []
    with open('2_index.csv', encoding='utf-8') as csvfile_1:
        writer = csv.reader(csvfile_1)
        for row in writer:
            if np.shape(row) == (3,):
                res = re.findall(r'\{\'(.*?)\'\}', row[2])
                index_3_title_1.append(row[0])
                index_3_title_2.append(row[1])
                index_3_link.append(res[0])
    # 对link列表进行转置
    tran_link = np.transpose(index_3_link)
    tran_titl_1 = np.transpose(index_3_title_1)
    tran_titl_2 = np.transpose(index_3_title_2)
    for i in range(np.shape(tran_link)[0]):
        # print(tran_titl_1[i], tran_titl_2[i], tran_link[i])
        get_page_content(tran_titl_1[i], tran_titl_2[i], tran_link[i])


def get_page_content(tran_titl_1, train_title_2, tran_link):
    site = session.get(tran_link)
    #  查看页面内容
    classifys = site.html.find('.info-block-main')  # 使用CSS选择器选择内容
    for classify in classifys:
        print('爬虫得到内容如下')
        classify_main = classify.text
        print(classify.text)  # 获取分类标题
        save2csc(tran_titl_1, train_title_2, classify_main)


def save2csc(tran_titl_1, train_title_2, classify_main):
    # header = ['classify_title', 'url']
    # writer.writerow(header)
    csvrow = []
    csvrow.append(tran_titl_1)
    csvrow.append(train_title_2)
    csvrow.append(classify_main)
    writer.writerow(csvrow)

if __name__ == '__main__':
    get_url_in_file()
    print("处理结束")
    op.close()

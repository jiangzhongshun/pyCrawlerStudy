# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2021/3/11 14:50
# !@Author : 提不动刀的胖虎
# !@File :.py


# 1.导入第三方库，模块requests  pip install requests

import requests
import parsel


def download_one_chapter(url):
    # 2.确定爬取的url

    response = requests.get(url)
    # 解决乱码问题
    response.encoding = response.apparent_encoding
    # print(response.text)

    # 3.对内容进行解析
    # 解析方法：1.正则表达式：通常式在linx下进行的，用于抒写我们爬取内容的规则
    # 2.xpath:用于解析xml文档内容解析
    # 3.css选择器
    # 4.parsel爬虫框架scrapy框架的核心组件

    # 将网页字符串转变成一个对象
    sel = parsel.Selector(response.text)
    # 获取章节的标题内容
    h1 = sel.css('h1::text')  # 返回值h1是个对象
    # h1标签选择器， ::伪类选择器
    title = h1.get()
    # print(title)

    # 获取章节内容
    content = sel.css('#content::text')  # #content id选择器
    lines = content.getall()
    # print(lines)

    # 将列表转换成字符串
    text = ""
    for line in lines:
        text += line.strip() + '\n'
   # print(text)

    # 4保存数据
    # 把所有章节放在一个文件中，mode='w'改成a a代表是append
    with open(file = '完美至尊', mode='a', encoding='utf-8') as f:
        f.write(title)
        f.write(text)



# 5.获取所有章节的网址
response = requests.get('https://www.5ibiquge.com/8_8119/')

    # 防止乱码出现
response.encoding = response.apparent_encoding

sel = parsel.Selector(response.text)

    # 6.开始抓取章节网址
dd_a = sel.css(' dd > a::attr(href)')
url_s = dd_a.getall()

for url in url_s[12:]:
    print(url)
    # 反复调取爬虫的方法即可
    download_one_chapter('https://www.5ibiquge.com'+url)
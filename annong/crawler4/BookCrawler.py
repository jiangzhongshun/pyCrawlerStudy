# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/12 20:17
# !@Author : 提不动刀的胖虎
# !@File :.py
import requests
from bs4 import BeautifulSoup

from model.Book import Book
from service.BookService import BookService


class BookCrawler:


    # https://www.136book.com/chuanyue/
    def getBookInfoCrawler(self, url):

        # 1.首先确定url，获取源码，一般还需要解析浏览器内核，这里不需要了
        # url = "https://www.136book.com/chuanyue/"

        # 解析这个网页的html网页，并采集有效的信息，
        # 获取html的代码，利用的爬虫利器requests

        requ = requests.get(url)


        # 进行格式转换
        # lxml是一个Python库，使用它可以轻松处理XML和HTML文件，还可以用于web爬取。市面上有很多现成的XML解析器，但是为了获得更好的结果，开发人员有时更愿意编写自己的XML和HTML解析器。这时lxml库就派上用场了。这个库的主要优点是易于使用，在解析大型文档时速度非常快，归档的也非常好，并且提供了简单的转换方法来将数据转换为Python数据类型，从而使文件操作更容易。

        # 需要导bs4和lxml架包
        soup = BeautifulSoup(requ.text, "lxml")

        # 2.获取哪些数据
            # 获取书本的信息的集合
        bookInfo = soup.find_all("td", class_="class_tdbg_760")

            # 创建一个列表来存每一本书
        bookList = []

        for binfo in bookInfo:

            # 1.1获取书名，对书名非空进行判断
            if(binfo.img !=None):

                bookName = binfo.img["alt"]

                # 1.2对书的封面的图片的链接进行爬取
                bookImgSrc = binfo.img["src"]

                pass

                # 1.3获取书本内容的超链接，它不在td标签里面,是在<strong>标签内的
            if(binfo.strong !=None):

                bookHref = binfo.strong.a["href"]

                pass

            # 1.4获取书本的作者
                # 通过len（）这个方法对p标签中的内容进行解析

            if(len(binfo.find_all("p"))>0):

                bookAuthor = binfo.find_all("p")[0].text.split(":")[-1]
                pass

                # 3.封装一个实体类
                bookList.append(Book(bookName, bookImgSrc, bookHref, bookAuthor))



            pass

        return bookList
        pass




    pass

if __name__ == '__main__':

    bookList = BookCrawler().getBookInfoCrawler()
    BookService().doSaveCrawlerDataToDB(bookList)
    print(bookList)
    pass
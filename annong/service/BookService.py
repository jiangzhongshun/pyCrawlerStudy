# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/14 14:25
# !@Author : 提不动刀的胖虎
# !@File :.py
from dao.BookDao import BookDao


class BookService:


    global dao
    dao = BookDao()

    # 1.存储爬虫的数据
    def doSaveCrawlerDataToDB(self, bookList):

        return dao.doSaveCrawlerDataToDB(bookList)
        pass

    # 2.全查数据
    def doFindAllBook(self):

        return dao.doFindAllBook()
        pass
    pass
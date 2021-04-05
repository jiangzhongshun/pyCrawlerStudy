# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/12 21:20
# !@Author : 提不动刀的胖虎
# !@File :.py

class Book:

    def __init__(self, bookName, bookImgSrc, bookHref, bookAuthor):

        self.bookName = bookName
        self.bookImgSrc = bookImgSrc
        self.bookHref = bookHref
        self.bookAuthor = bookAuthor
        pass

    def __str__(self):

        return "图书名称：{0}，图书图片：{1}，图书内容：{2}，图书作者：{3}".format(self.bookName, self.bookImgSrc, self.bookHref, self.bookAuthor)
        pass

    __repr__ = __str__

    pass
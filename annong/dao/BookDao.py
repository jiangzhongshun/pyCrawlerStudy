# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/14 14:28
# !@Author : 提不动刀的胖虎
# !@File :.py
from util.Dbutil import Dbutil


class BookDao:

    # 1.存储爬虫的数据
    def doSaveCrawlerDataToDB(self, bookList):

        try:
            conn = Dbutil().getConn()

            cursor = conn.cursor()

            for book in bookList:

                sql ="insert into tb_book(bookname, bookimgsrc, bookhref, bookauthor) values ('%s','%s','%s','%s')"

                data =(book.bookName, book.bookImgSrc, book.bookHref, book.bookAuthor)

                cursor.execute(sql%data)

                conn.commit()
                pass
            print("dao保存数据成功")
            return True
            pass
        except:
            print("保存失败")
            return False
            pass
        pass


    # 2.全查
    def doFindAllBook(self):

        try:

            conn = Dbutil().getConn()

            cursor = conn.cursor()

            sql = "select * from tb_book"

            cursor.execute(sql)

            result = cursor.fetchall()
            return result

            pass
        except:
            pass
        pass
    pass
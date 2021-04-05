# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/13 9:17
# !@Author : 提不动刀的胖虎
# !@File :.py
import pymysql


class Dbutil:

    # 将pycharm后台与mysql连接
    def getConn(self):

        # 如何导架包，理解架包,有的最底层的架包加载不进去的，介绍导包pymysql
        # 目的是连接数据库
        conn =pymysql.Connect(host="127.0.0.1", port=3307, user="root", password="123456", db="python", charset="utf8", cursorclass= pymysql.cursors.DictCursor)

        print("数据库连接成功")
        return conn

        pass


    pass

if __name__ == '__main__':

    Dbutil().getConn()
    pass
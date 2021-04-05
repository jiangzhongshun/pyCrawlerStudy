# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/13 11:14
# !@Author : 提不动刀的胖虎
# !@File :.py
from util.Dbutil import Dbutil


class UserDao:

    # 1.实现用户登录得dao 层
    def doLogin(self, loginUser):

        try:
            # 1.获取到数据库得连接对象
            conn = Dbutil().getConn()

            # 2.获取到数据库游标的对象cursor
            cursor = conn.cursor()

            # 3。创建sql
            sql = "select * from tb_user where username='%s' and password='%s'"

            # 5.对sql中的%s进行设值
            data = (loginUser.username, loginUser.password)

            # 6.执行sql
            cursor.execute(sql % data)

            # 7.得到执行结果集
            num = cursor.rowcount
            return num
            pass
        except:
            print("发生异常")
            return 0
            pass

        pass

    # 2.实现全查
    def doFindAllUser(self):

        try:

            # 1.获取到数据库的连接
            conn = Dbutil().getConn()

            # 2.获取到游标对象cursor对象
            cursor = conn.cursor()

            # 3.创建sql
            sql = "select * from tb_user"

            # 4.执行sql
            cursor.execute(sql)

            # 5.得到结果集
            result = cursor.fetchall()
            return result

            pass
        except:

            print("dao层报错")
            pass

        pass

    # 3.实现用户增加
    def doAdduser(self,newUser):

        try:

            # 1.获得数据库的连接
            conn = Dbutil().getConn()

            # 2. 获得游标的对象
            cursor = conn.cursor()

            # 3.创建sql
            sql = "insert into tb_user (username,password) values ('%s','%s')"

            # 4.对参数设值
            data = (newUser.username, newUser.password)

            # 5.执行sql
            cursor.execute(sql%data)

            # 6.提交事务
            conn.commit()
            return True
            pass
        except:
            print("dao报错")
            return False
            pass
        pass

    # 4.实现用户删除
    def doDeletUser(self,id):

        try:
            # 1.获取数据库的连接对象
            conn = Dbutil().getConn()

            # 2.获取游标
            cursor = conn.cursor()

            # 3.创建sql
            sql = "delete from tb_user where id='%s'"

            # 4.参数设值
            data = (id)

            # 5执行sql
            cursor.execute(sql%data)

            # 6.提交事务
            conn.commit()

            return True
            pass
        except:

            print("dao层删除失败")
            return False
            pass
        pass

    # 5.实现修改回显，条件查询
    def doFindUserById(self, id):

        try:

            conn = Dbutil().getConn()

            cursor = conn.cursor()

            sql = "select * from tb_user where id ='%s'"

            data = (id)

            cursor.execute(sql % data)

            result = cursor.fetchall()
            return result
            pass
        except:
            print("dao查询报错")
            pass
        pass

    # 6.实现修改的功能
    def doUpdateUser(self,oldUser):

        try:

            conn = Dbutil().getConn()

            cursor = conn.cursor()

            sql = "update tb_user set username='%s',password='%s' where id='%s'"

            id1 =int(oldUser.get("id"))

            data = (oldUser.username, oldUser.password, id1)

            cursor.execute(sql % data)

            count = cursor.rowcount

            conn.commit()
            return count
            pass
        except:
            print("dao层报错")
            return 0
            pass
        pass

    # 7.全文搜索，模糊查询
    def doFindUserByName(self,searchName):

        try:

            conn = Dbutil().getConn()

            cursor = conn.cursor()

            sql = "select * from tb_user where username like '%"+searchName+"%'"


            cursor.execute(sql)

            result =cursor.fetchall()

            return result

            pass
        except:
            pass
        pass



    pass
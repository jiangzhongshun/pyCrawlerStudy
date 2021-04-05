# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/13 11:11
# !@Author : 提不动刀的胖虎
# !@File :.py
from dao.UserDao import UserDao


class UserService:


    # 全局对象
    global dao
    dao = UserDao()

    # 1.实现用户登录得服务
    # loginUser 参数代表当前用户
    def doLogin(self, loginUser):

        num = dao.doLogin(loginUser)

        if (num>0):
            print("登录成功service层OK")
            return True
            pass
        else:
            print("登录失败。service层返回空值")
            return False
            pass
        pass

    # 2.实现用户管理的数据显示
    def doFindAllUser(self):
        return dao.doFindAllUser()
    
    # 3.实现用户增加
    def addUser(self, newUser):

        return dao.doAdduser(newUser)
        pass

    # 4.实现删除
    def deletUser(self,id):

        return dao.doDeletUser(id)
        pass

    # 5.实现修改的回显
    def FindUserById(self, id):

        return dao.doFindUserById(id)

        pass

    # 6.实现修改的功能
    def doUpdateUser(self, oldUser):

        return dao.doUpdateUser(oldUser)
        pass

    # 7.全文搜索
    def doFindUserByName(self,searchName):

        return dao.doFindUserByName(searchName)
        pass
    pass
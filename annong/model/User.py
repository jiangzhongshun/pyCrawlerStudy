# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/13 9:01
# !@Author : 提不动刀的胖虎
# !@File :.py



class User:


    # (1)构造方法：目的是为了创建对象
    def __init__(self, id, username, password):

        self.id = id
        self.username = username
        self.password = password
        pass

    # (2)str方法重写，展示给别人看，打印作用
    def __str__(self):

        return "id={0},username={1},password={2}".format(self.id, self.username, self.password)
        pass

    # (3)开发者用，目的为了白盒测试
    __repr__ = __str__
    pass

if __name__ == '__main__':
    print(User(1, "俞非鱼", "123456"))
    pass
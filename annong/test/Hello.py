# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2020/2/13 9:48
# !@Author : 提不动刀的胖虎
# !@File :.py


import web


 # 1.url的映射路径
urls = (

    # hello对应下面的类
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
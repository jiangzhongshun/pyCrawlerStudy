import web
import pymysql

#  渲染当前项目的前端页面
render = web.template.render("templates")

# 映射路径

urls = (
    "/login", "login",
)

# 3.把当前的urls交给我我们web容器
app = web.application(urls, globals())

class login:

    # 向我们服务器发起请求
    def GET(self):
        return render.login()

    pass

    def POST(self):
        # 获取用户的请求参数
        loginUser = web.input()

        print(loginUser.username)
        print(loginUser.password)
        # 连接数据库，获得连接
        conn = pymysql.Connect(host="127.0.0.1", port=3306, user="root", password="123", db="python", charset="utf8",
                               cursorclass=pymysql.cursors.DictCursor)
        print("数据库连接成功")
        # 通过数据库的连接对象获取游标
        cursor = conn.cursor()

        # 创建sql
        sql = "select * from tb_user where username='%s'and password='%s'"

        # 对占位符设置，创建数据对象
        data = (loginUser.username, loginUser.password)

        # 执行sql
        cursor.execute(sql % data)

        # 得到结果
        num = cursor.rowcount
        print(num)
        pass

    pass

if __name__ == '__main__':
    app.run()

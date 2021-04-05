import web
import pymysql

#  渲染当前项目的前端页面
render = web.template.render("templates")

urls = (
    "Hello", "Hello"
)

app = web.application(urls, globals())

class Hello:
    def GET(self):
        return render.Hello()
    pass

if __name__ == '__main__':
    app.run()
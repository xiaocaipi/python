#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
from _elementtree import parse
from dataguru.week4 import otherclass


#注册一个模板文件夹  
render = web.template.render('templates/')

# base 作为主模板
#render = web.template.render('templates/',base='base')

#设置模板的全局变量，就可以再模板里面调用了,返回数据库连接的对象 
web.template.Template.globals['render'] = render 

#配置数据库
db = web.database(dbn='mysql', host='192.168.1.32',port=3306,user='root', pw='', db='test') 
       
urls = (
    '/findpassword', 'findpassword',    
    '/tofindpassword', 'tofindpassword',
    '/toregister', 'toregister',
    '/tocheckmail', 'tocheckmail',
    '/checkmail', 'checkmail',
    '/register', 'register',
    '/main', 'main',
    '/index', 'index',
    '/toLogin', 'toLogin',
    '/login', 'login',
    '/database', 'database',
    '/otherclass', 'otherclass',
    '/seeother', 'seeother',
    '/(test1|test2)', 'test',
    '/formpage', 'formpage',
    '/formdeal', 'formdeal',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())


class main:
    def GET(self):
        return render.main()
    
class toregister:
    def GET(self):
        return render.login('register')
    
class register:
    def GET(self):
        pars = web.input()
        username = pars['username']
        password = pars['password']
        email = pars['email']
        db.insert('user',username=username,password=password,email=email)
        return pars
    def POST(self):
        return self.GET()
    
class toLogin:
    def GET(self):
        return render.login('login')
    
class login:
    def GET(self):
        pars = web.input()
        username = pars['username']
        password = pars['password']
        rt = db.query('select * from user where username=$aa', vars={'aa':username})
        for r in rt:
            dbpassword = r['password']
            if password ==dbpassword:
                return render.loginresult('1')
            else: 
                return render.loginresult('0')
    def POST(self):
        return self.GET()

class tocheckmail:
    def GET(self):
        return render.checkmail()
    
class checkmail:
    def GET(self):
        pars = web.input()
        username = pars['username']
        rt = db.query('select * from user where username=$aa', vars={'aa':username})
        for r in rt:
            email = r['email']
            from sendmail import send_mail
            return send_mail(email, 'checkmail', 'please checkmail http://localhost:8080/checkingmail')
            
    def POST(self):
        return self.GET()

class tofindpassword:
    def GET(self):
        return render.findpassword()
class findpassword:
    def GET(self):
        pars = web.input()
        username = pars['username']
        rt = db.query('select * from user where username=$aa', vars={'aa':username})
        for r in rt:
            password = r['password']
            email = r['email']
            content ='your password is '+password
            from sendmail import send_mail
            return send_mail(email, 'findpassword', content)
            
    def POST(self):
        return self.GET()
        

class database:
    def GET(self):
        #数据库查询  
        rt =  db.select('stockcode_base' ,limit ='0,10')
        for r in rt:
            print r
        return '200'
            

class index:
    #第一个没有参数 是因为没有括弧 没有正则表达式    
    def GET(self):
        #获取参数
#         par = web.input()
        
        #return par
        
        #返回html的内容
        #return '<h1>i m index </h1>'
        
         #这个就是返回一个模板  ，render 是模板文件夹 定义的，post 是模板文件夹下的 html 等文件名 不带后缀的
        # return render.post();
       
        #测试模板文件带参数的 需要传参数
        #return render.testWithoutpar('<h1>dataguru</h1>');
        
        #返回sub 页面 ，render 是有base 模板的
        #return render.sub()
        
        return render.testWithoutpar('aaa')
        
#定义一个seeother跳转到 index    
class seeother:
    def GET(self):
        raise web.seeother('/index')

class test:  
     #第二个没有参数 是因为用过了正则表达式，有括弧的会把url 匹配到的部分作为一个参数传给它，如果上面有2个括弧，那么下面有2个参数   
     #参数的值就是正则表达式匹配到的值，比如是test1 匹配到了那么name就是test1        
    def GET(self, name):
        
        return 'im %s' % name
    
    def POST(self, name):
        #return 'i am post request'
        return "name:%s,paras:%s" %(name,web.input())
    def DEL(self, name):
        pass
        
    

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'
    def POST(self):
        #导入sendmail。py 的send_mail 方法
        from sendmail import send_mail
        return send_mail('xiaocaipi@qq.com', 'test', 'test111')

class formpage:
    def GET(self):
        #这个就是返回一个模板  ，render 是模板文件夹 定义的，post 是模板文件夹下的 html 等文件名 不带后缀的
        return render.post();

class formdeal:
    def GET(self):
        pars = web.input()
        print pars
        return pars
    def POST(self):
        return self.GET()

if __name__ == "__main__":
    app.run()

#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
from config.settings import *
from utils.db_util import _create_db
db = _create_db()
type = 1

class database:
    def GET(self):
        rt = db.select('20w', limit='0,10')
        for r in rt:
            print r
        return '200'

class index:
    def GET(self):
        #return 'i am index page'
        #return render.testWithPar('dataguru')
        
        #这里就是先获取session
        session = web.config._session
        print session.status
        #修改session的status 这个值
        session.status = 1
        print session.status
        #先获取cookie
        cookies = web.cookies()
        print cookies
        #设置cookie
        web.setcookie('id', '9527')
        return render.testWithoutPar()
        #return render.sub()

class test:
    def GET(self, name):
        try:
            a = 1/0
        except Exception, e:
            print 'e:',e
            print 'message:', e.message
            import traceback
            traceback.print_exc()
            trace = traceback.extract_stack()
            print trace
            info = traceback.format_exc()
            print info
            import sys
            info = sys.exc_info()
            print info
        return 'i am %s page' % name

class formpage:
    def GET(self):
        return render.post()

class formdeal:
    def GET(self):
        pars = web.input()
        print pars
        return pars

    def POST(self):
        from utils.file_upload import save_file
        save_file()
        return self.GET()

class default:
    def GET(self, name):
        # print web.ctx.env, web.ctx.status
        # web.header('Cache-Control', 'no-cache')
        raise web.seeother('/error?error_msg=error test')
        if not name:
            name = 'Xiaowu'
        return 'Hello, ' + name + '!'

    def POST(self, name):
        #return 'i am in POST'
        #return do_action('***') + 'action line' + do_action('***')
        from utils.sendmail import send_mail
        return send_mail('send_to', 'subject', 'body')
        #return self.GET(name)

class error:
    def GET(self):
        pars = web.input()
        return render.error(pars.get('error_msg'))

class Hello:
    def GET(self):
        return render.hello()

class main:
    def GET(self):
        return render.main(type)
    
class toregister:
    def GET(self):
        return render.login(('register',type))
    
class register:
    def GET(self):
        print 111
        pars = web.input()
        print pars
        username = pars['username']
        password = pars['password']
       
        email = pars['email']
        db.insert('user',username=username,password=password,email=email)
        return render.loginresult('3')
    def POST(self):
        print 111
        return self.GET()
    
class toLogin:
    def GET(self):
        return render.login(('login',type))
    
class login:
    def GET(self):
        pars = web.input()
        username = pars['username']
        password = pars['password']
        rt = db.query('select * from user where username=$aa', vars={'aa':username})
        for r in rt:
            dbpassword = r['password']
            if password ==dbpassword:
                session = web.config._session
                session.status='1'
                return render.loginresult('1')
            else: 
                return render.loginresult('0')
    def POST(self):
        return self.GET()

class tocheckmail:
    def GET(self):
        return render.checkmail(type)
    
class checkmail:
    def GET(self):
        pars = web.input()
        username = pars['username']
        rt = db.query('select * from user where username=$aa', vars={'aa':username})
        for r in rt:
            email = r['email']
            from utils.sendmail import send_mail
            return send_mail(email, 'checkmail', 'please checkmail http://localhost:8080/checkingmail')
            
    def POST(self):
        return self.GET()

class tofindpassword:
    def GET(self):
        return render.findpassword(type)
class findpassword:
    def GET(self):
        pars = web.input()
        username = pars['username']
        rt = db.query('select * from user where username=$aa', vars={'aa':username})
        for r in rt:
            password = r['password']
            email = r['email']
            content ='your password is '+password
            from utils.sendmail import send_mail
            return send_mail(email, 'findpassword', content)
            
    def POST(self):
        return self.GET()

class todetail:
    def GET(self):
        session = web.config._session
        print session.status
        if('1'== session.status):
            return render.detail(type)
        else:
            return render.loginresult('4')
        
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
#导入之前的url
from config.url import urls
#导入之前请求的处理类
from views.index import *

from utils.db_util import _create_db
db = _create_db()

##设置python环境为utf-8编码
import sys
print 'default python env coding:', sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print 'current python env coding:', sys.getdefaultencoding()

##session配置   session 是以cookie 中sessioid 存起来的  所以这里设置的是cookie
web.config.session_parameters['cookie_name'] = 'webpy_session_id'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 86400, #24 * 60 * 60, # 24 hours   in seconds
web.config.session_parameters['ignore_expiry'] = True
#忽略是否改了ip
web.config.session_parameters['ignore_change_ip'] = True
#是否用https保存的
web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
web.config.session_parameters['expired_message'] = 'Session expired'

app = web.application(urls, globals())
if web.config.get("_session") is None:
    from web import utils
    #session 存在sessions 的目录下
#   store = web.session.DiskStore('sessions')
    
    store = web.session.DBStore(db, 'sessions')
    #用户信息 user 是这样的
    user = utils.Storage({
                          "id": "",
                          "name": "",
                          "email": "",
                          "privilege": "",
                          "image_url": "",
                          })
    #把应用和session绑定，绑定还要选存储的方式，这里store 是 磁盘   第三个 是初始化的值，就应用需要初始化的信息，这里初始化了状态和用户信息
    session = web.session.Session(app, store,
                                  initializer={
                                               "status": 0,
                                               "user": user,
                                               })
    #把session 赋值到 web.config._session  在其他地方只要 用 web.config._session  就能取到session
    web.config._session = session
else:
    session = web.config._session

if __name__ == "__main__":
#     web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)   ##这行是新增的
    app.run()

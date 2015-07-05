#!/usr/bin/python
# -*- coding: utf-8 -*-
import web

##session配置
web.config.session_parameters['cookie_name'] = 'webpy_session_id'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 86400, #24 * 60 * 60, # 24 hours   in seconds
web.config.session_parameters['ignore_expiry'] = True
web.config.session_parameters['ignore_change_ip'] = True
web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
web.config.session_parameters['expired_message'] = 'Session expired'

app = web.application(urls, globals())
if web.config.get("_session") is None:
    from web import utils
    store = web.session.DiskStore('sessions')
    user = utils.Storage({
                          "id": "",
                          "name": "",
                          "email": "",
                          "privilege": "",
                          "image_url": "",
                          })
    session = web.session.Session(app, store,
                                  initializer={
                                               "status": 0,
                                               "user": user,
                                               })
    web.config._session = session
else:
    session = web.config._session


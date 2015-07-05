#!/usr/bin/env python
#coding=utf-8
import web, settings, traceback

urls = (
    '([a-zA-Z0-9_\%\/]*)', 'dispatcher'
    )

class dispatcher:
    def __init__(self):
        pass

    def GET(self, path):
        return self.__request(path)

    def POST(self, path):
        return self.__request(path)

    def __request(self, path=''):
        try:
            if path.count('/') < 2:
                path = settings.DEFAULT_PATH
            path_list = path.strip()[1:].split('/', 2)
            modelName, controllerName = path_list[:2]
            if len(path_list)>2:
                pars = path_list[2]
            else:
                pars = ''
    #             print 'pars:', pars
            if not controllerName:
                controllerName = 'index'
            if not modelName or not controllerName:
                return 'model/controller missing'
            moduleList = __import__('action.' + modelName, {}, {}, [modelName])
            modelObj = getattr(moduleList, modelName)(pars)
            if hasattr(modelObj, controllerName):
                result = getattr(modelObj, controllerName)()
            else:
                result = 'no controller'
            return result
        except Exception ,e:
            traceback.print_exc()
            debug_info = traceback.format_exc().replace('\n', '<br>')
            msg = 'Error Message: %s <br> %s' % (e.message, debug_info)
            from action.base import base as baseAction
            baseObj=baseAction()
            if e.message == 'db not exists' :
                return baseObj.error('尚未安装',baseObj.makeUrl('install'))
            return baseObj.error(msg,baseObj.makeUrl('index'))
            # raise Exception,msg

def session_hook():
    web.ctx.session = session

import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

if __name__ == "__main__":
    app = web.application(urls, globals())
    #web.header("Content-Type","text/html; charset=utf-8")
    web.config.session_parameters['cookie_name'] = 'py_wpcms_sid'
    web.config.session_parameters['cookie_domain'] = None
    web.config.session_parameters['timeout'] = 86400,
    web.config.session_parameters['ignore_expiry'] = True
    web.config.session_parameters['ignore_change_ip'] = True
    web.config.session_parameters['secret_key'] = 'JJIEhi323rioes34hafwaj2'
    web.config.session_parameters['expired_message'] = 'Session expired'
    session = web.session.Session(app, web.session.DiskStore('data/sessions'), initializer={'login': False, 'user_info':{}})
    def session_hook():
        web.ctx.session = session
    app.add_processor(web.loadhook(session_hook))
    app.run()
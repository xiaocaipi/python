#!/usr/bin/env python
#coding=utf-8
import web, settings, traceback

urls = (
    '([a-zA-Z0-9_\%\/]*)', 'dispatcher'
    )
#用分发器来处理对象   但要设定要url 规则 这里是 localhost/index/index   这样的  模块/分发器   
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
            #动态导入这个模块的类  这里例子是导入 action.index.py  里面的index 类     这里 类名 和模块名一样
            moduleList = __import__('action.' + modelName, {}, {}, [modelName])
            modelObj = getattr(moduleList, modelName)(pars)
            if hasattr(modelObj, controllerName):
                #调用模块里的 类里的方法  这里是 index 类里的  index 方法
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
    session = web.session.Session(app, web.session.DiskStore('data/sessions'), initializer={'login': False})
    def session_hook():
        web.ctx.session = session
    app.add_processor(web.loadhook(session_hook))
    app.run()
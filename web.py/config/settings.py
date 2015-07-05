#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
import os

##设置为debug模式
web.config.debug = True
web.config['work_dir'] = os.getcwd()


##模板文件夹定义
render = web.template.render('templates/')

config = web.storage(
    email='chenxiaowu@dangdang.com',
    site_name = 'dataguru 课程',
    site_desc = '',
    site_auther = 'XiaowuChen',
    resources = '/static',
)

##设置模板全局变量
web.template.Template.globals['render'] = render
web.template.Template.globals['site_config'] = config
#web.template.Template.globals['db'] = db
#web.template.Template.globals['session'] = web.config._session
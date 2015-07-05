#!/usr/bin/python
# -*- coding: utf-8 -*-

import web

def send_mail(send_to,subject,body,cc=None,bcc=None):
    try:
        web.config.smtp_server = 'smtp.qq.com' 
        web.config.smtp_port = 25 
        web.config.smtp_username = 'xiaocaipi@qq.com' 
        web.config.smtp_password = '0410149253cai' 
        web.config.smtp_starttls = True 
        send_from ="xiaocaipi@qq.com"
        web.sendmail(send_from, send_to, subject, body)
        return 1

    except Exception, e:
        print e
        return -1

a = send_mail('xiaocaipi@qq.com', 'test1', 'test1111')
print a
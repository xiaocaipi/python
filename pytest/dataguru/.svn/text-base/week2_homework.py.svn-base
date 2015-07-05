#!/usr/bin/python
#-*-coding:utf-8-*-
import getpass
import os
import hashlib
from Tkinter import Place
from _ast import Num
from argparse import Action

class userinfo:
    def __init__(self, account, age, city):
        self.account = account
        self.age = age
        self.city = city

    def description(self):
        print('账号:'+self.account)
        print('年龄:'+self.age)
        print('城市:'+self.city)
        
def register():
    print('开始注册')
    account = raw_input('请输入用户名:')
    age = raw_input('请输入年龄:')
    password = hashlib.md5(getpass.getpass('请输入密码:').encode('utf-8')).hexdigest()
    secondpassword = hashlib.md5(getpass.getpass('请再输入密码:').encode('utf-8')).hexdigest()
    place = raw_input('请输入地方:')
    if(password ==secondpassword):
        try:
            fileobject = open('userinfo.txt','a')
            fileobject.write("\n"+account+"\t"+"\t"+age+"\t"+place)
            fileobject.close
            fileobject1 = open('password.txt','a')
            fileobject1.write("\n"+account+"\t"+"\t"+password)
            fileobject1.close
        except:
            print('打开文件错误')
            fileobject.close()
            return None
    else:
        print('2次密码不一致')
        
        
    
    

def inputinfo():
    account = raw_input('请输入账号:')
    password = hashlib.md5(getpass.getpass('请输入密码:').encode('utf-8')).hexdigest()
    return account, password

def getinfodict():
    try:
        fileobject = open('userinfo.txt','r')
    except:
        print('打开文件错误')
        fileobject.close()
        return None

    infodict = {}
    for line in fileobject:
        list = line.split()
        if len(list)!=0:
            user = userinfo(list[0], list[1], list[2])
            infodict.setdefault(user.account, user)
    fileobject.close()
    return infodict

def checkpassword(username, password):
    try:
        fileobject = open('password.txt','r')
    except:
        print('打开文件错误')
        fileobject.close()
        return None

    for line in fileobject:
        list = line.split()
        if len(list)!=0 and   username == list[0] and password == list[1]:
            fileobject.close()
            return True
    fileobject.close()
    return False

def printuser():
    infodic = getinfodict()
    print('------------------用户---------------')
    for key in infodic.keys():
        print(key)
    key = raw_input('-------请输入您要查询的用户账号------\n')
    if infodic.get(key):
        user = infodic[key]
        user.description()
    else:
        print('输入错误，没有此账号')


haslogin = False
def start():
    global haslogin 
    action = raw_input('1:注册     2:登陆   3:查看用户')
    if action == '1':
        register()
        start()
    else:
        if  action =='2':
            account, password = inputinfo()
            if checkpassword(account, password):
                haslogin = True
                print("登陆成功")
                start()
            else:
                print('账号或密码错误')
                start()
        elif action == '3' and haslogin:
            printuser()
        else:
            start()
            
            
        

if __name__ == '__main__':
    start()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import test.hello as hello

hello.test()

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

class Student2(object):
    
    def __init__(self):
        #python中的第一次赋值视为变量的定义！
        self._birth = 1

    def get_birth(self):
        return self._birth


    def set_birth(self, value):
        self._birth = value
    def age(self):
        return 2014 - self._birth
bart = Student('Bart Simpson', 59)
print(bart.name)
bart2 = Student2()
bart2.set_birth(11)
print(bart2.get_birth())
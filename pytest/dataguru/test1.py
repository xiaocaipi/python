#!/usr/bin/python
# -*- coding: utf-8 -*-
#########内省############
class MyClass(object):
    def __init__(self):
        pass
    def __del__(self):
        pass
    def foo(self):
        print 'in foo'
    def __str__(self):
        return 'myclass str'
        
mycls = MyClass()
print id(mycls)
print str(mycls)
print dir(mycls)
print help(mycls)
print type(mycls)
print hasattr(mycls, 'foo')
print getattr(mycls, 'foo')
print isinstance(mycls, MyClass)
print isinstance(mycls, object)
    
    
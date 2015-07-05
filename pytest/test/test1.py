#coding:utf-8
import os
print 'The quick brown fox', 'jumps over', 'the lazy dog'
#name = raw_input()
#print name
a='I\'m \"OK\"!'
print a
print r'\\\t\\'
a=cmp(1, 2)
print a
print [d for d in os.listdir('c:')]

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
def format(orgin):
    return orgin.capitalize()
a=map(format, ['adam', 'LISA', 'barT'])
print a
#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
a=reduce(lambda x,y: x*y, [1,2,3,4])
print a
def prod(x,y):
    return x*y
a=reduce(prod, [1,2,3,4])
print a

s = r'ABC\\-001' 
print s
        
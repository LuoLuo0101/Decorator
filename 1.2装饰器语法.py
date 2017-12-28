# -*- coding: utf-8 -*-
# @Time    : 12/28/17 1:30 PM
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : b.py
# @Software: PyCharm
"""
Python2.5加入的@语法

执行顺序
1、先走 @decorated_by，参数为被装饰的方法对象
2、然后执行装饰器这个方法 decorated_by，并返回被装饰的方法对象
3、然后走到调用被装饰的方法的位置，执行被装饰的方法，返回被装饰的方法的返回值
4、每装饰一个方法，装饰器方法都会执行一遍
5、如果同时用多个装饰器去装饰一个方法，会按照从上到下的顺序扫描，但是实际工作中，装饰器采用从下到上的顺序执行
"""


def decorated_by(func):
    func.__doc__ += "\n Decorated by decorated_by"
    return func


def also_decorated_by(func):
    func.__doc__ += "\n Decorated by decorated_by"
    return func


@also_decorated_by
@decorated_by
def add(x, y):
    """1234"""
    # add = also_decorated_by(decorated_by(add))
    return x + y


@decorated_by
def sub(x, y):
    """1234"""
    # sub = decorated_by(sub)
    return x - y


@decorated_by
def aha(x, y):
    """1234"""
    return x * y


print(add(1, 2))
print(sub(1, 2))
print(aha(1, 2))
print("111")
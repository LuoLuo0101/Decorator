# -*- coding: utf-8 -*-
# @Time    : 12/28/17 5:42 PM
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : 1.6.2执行时封装代码.py
# @Software: PyCharm


import functools


def decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        """inner的帮助信息"""
        return func(*args, **kwargs)

    return inner


@decorator
def func(a, b):
    """func的帮助信息"""
    return a + b


print(func(1, 2))
print(func.__dict__)
print(func.__doc__)

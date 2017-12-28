# -*- coding: utf-8 -*-
# @Time    : 12/28/17 9:46 AM
# @Author  : wangge
# @Email   : ge.wang@easytransfer.cn
# @File    : 1.1理解装饰器.py
# @Software: PyCharm
"""修改原来函数的__doc__，并返回原先函数对象"""


def decorated_by(func):
    func.__doc__ += "\n Decorated by decorated_by"
    return func


def add(x, y):
    """1234"""
    return x + y


add = decorated_by(add)

# -*- coding: utf-8 -*-
# Auther : 戚
# Date : 2023/5/16 21:34
# File : grm.py
# Description :
import keyword

print(keyword.kwlist)


def code(self, expect):
    """

    :param self:
    :param expect:
    :return:
    """


# 元组
x = (1, 2)
print("x:", type(x))
# 数字，字符串，列表，元组，字典，集合
# 列表
y = ['1', '2', '3']
print("y:", {type(y)})
# 字符串
z = "hello world"
print("z:", type(z))

# 集合
j = {"1", "2", "3"}
print("j:", type(j))

# 字典
d = {"1": "小米", "2": "huawei"}
print("y:", type(d))

# number
n = 1
print("y:", type(n))

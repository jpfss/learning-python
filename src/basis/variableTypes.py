# -*- coding: utf-8 -*-

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter)
print (miles)
print (name)
# =============================================================================
# Multiple Assignment
# =============================================================================

a = b = c = 1
a, b, c = 1, 2, "john"

print(a)
print(b)
print(c)

# =============================================================================
# Standard Data Types
# =============================================================================

# =============================================================================
# Python Numbers
# =============================================================================
# =============================================================================
# 数字类型-自动创建数字类型对象 
# =============================================================================
var1 = 1
var2 = 10
#用del删除引用
del var1
#无法打印该引用对象
#print(var1)

# =============================================================================
# Data Type Conversion
# =============================================================================

a = 100;

print("转换为int:"+str(int(a)))
print("转换为float:"+str(float(a)))
# 复数 complex number
print("转换为complex:"+str(complex(a)))
print("转换为str:"+str(a))
# 表达式字符串
print("转换为repr:"+repr(a))
# 计算一个字符串并返回一个对象。
# print("转换为eval:"+eval(str(a)))
# 元组
# print("转换为tuple:"+str(tuple(a)))
# 列表
# print("转换为list:"+list(a))
# set
# print("转换为set:"+str(set(a)))
# print("转换为frozenset:"+frozenset(float(a)))
# 字典
# print("转换为dict:"+dict(float(a)))

# chr 字符
print("转换为chr:"+chr(a))
# Unicode character unicode字符
# print("转换为ord:"+str(ord(a)))
# hex 十六进制字符串
print("转换为hex:"+hex(a))
# Oct 八进制字符串
print("转换为oct:"+oct(a))

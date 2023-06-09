# -*- coding: utf-8 -*-

# 申明
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

# 索引
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

# =============================================================================
# Updating Tuples
# =============================================================================
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print ("tup3 is %s"%(str(tup3)))
# =============================================================================
# Delete Tuple Elements
# =============================================================================
tup = ('physics', 'chemistry', 1997, 2000);

print (tup)
del tup;
print ("After deleting tup : ")
# 删除引用后，引用对象不存在会报错
# print (tup)

# =============================================================================
# Basic Tuples Operations
# =============================================================================
print(len((1, 2, 3)))
print((1, 2, 3) + (4, 5, 6))
print(('Hi!',) * 4)
print(3 in (1, 2, 3))
for x in (1,2,3) : print (x, end = ' ')
# =============================================================================
# Indexing, Slicing, and Matrixes
# =============================================================================
T=('C++', 'Java', 'Python')
print(T[2])
print(T[-2])
print(T[1:])
# -*- coding: utf-8 -*-
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
# key不存在，报错
# print ("dict['Alice']: ", dict['Alice'])


# =============================================================================
# Updating Dictionary
# =============================================================================
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
# =============================================================================
# Delete Dictionary Elements
# =============================================================================
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary
# 已经删除引用，打印报错
# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])
# =============================================================================
# Properties of Dictionary Keys 
# =============================================================================
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name'])
# =============================================================================
# Built-in Dictionary Functions and Methods
# =============================================================================
print(len(dict))
print(str(dict))
print(type(dict))
# -*- coding: utf-8 -*-

import os
print("Python is really a great language,", "isn't it?")

# =============================================================================
# The input Function
# =============================================================================
x = input("something:")
print("x:%s" % (x))
# =============================================================================
# Opening and Closing Files
# =============================================================================
# 到目前为止,您一直在读写标准输入和输出.
# 现在我们将看到如何使用实际的数据文件
# =============================================================================
# The open Function
# =============================================================================
# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()
# =============================================================================
# The close() Method
# =============================================================================
# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)

# Close opened file
fo.close()
# =============================================================================
# Reading and Writing Files
# =============================================================================
# Open a file
fo = open("foo.txt", "w")
fo.write("Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()
# =============================================================================
# The read() Method
# =============================================================================
# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print("Read String is : ", str)

# Close opened file
fo.close()
# =============================================================================
# File Positions
# =============================================================================
# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print("Read String is : ", str)

# Check current position
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print("Again read String is : ", str)

# Close opened file
fo.close()
# =============================================================================
# Renaming and Deleting Files
# =============================================================================

# Rename a file from test1.txt to test2.txt
os.rename("test1.txt", "test2.txt")
# =============================================================================
# The remove() Method
# =============================================================================

# Delete file test2.txt
os.remove("text2.txt")
# =============================================================================
# Directories
# =============================================================================

# Create a directory "test"
os.mkdir("test")
# The chdir() Method
# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")

# The getcwd() Method
# This would give location of the current directory
os.getcwd()
# The rmdir() Method
# This would  remove "/tmp/test"  directory.
os.rmdir("/tmp/test")

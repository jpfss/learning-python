# -*- coding: utf-8 -*-

import sys;

print ("Hello, Python!");

# =============================================================================
# Multi-Line Statements
# =============================================================================
item_one = 0
item_two = 1
item_three = 2
total = item_one + \
   item_two + \
   item_three

# print("total:"+total)

# =============================================================================
# The statements contained within the [], {}, or () brackets do not need to 
# use the line continuation character
# =============================================================================
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# =============================================================================
# Quotation
# =============================================================================
word = "word"
sentence = "This is sentence"
paragraph = """ This is a paragraph .
It is made up of multiple lines and sentences"""

# =============================================================================
# Waiting for the User
# =============================================================================

input("\n\nPress the enter key to exit.")

# =============================================================================
# comment
# =============================================================================
# This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.
name = "Madisetti" # This is again comment

# =============================================================================
# Multiple Statements on a Single Line
# =============================================================================
x = 'foo'; sys.stdout.write(x + '\n')

# =============================================================================
# Multiple Statement Groups as Suites
# =============================================================================
file_finish = "end"
file_text = ""
contents=[]

file_name=input("Enter filename: ")
if len(file_name) == 0:
   print("Please enter filename")
   sys.exit()

try:
   # open file stream
   file = open(file_name, "w")

except IOError:
   print ("There was an error writing to", file_name)
   sys.exit()

print ("Enter '", file_finish,)
print ("' When finished")

while file_text != file_finish:
   file_text = input("Enter text: ")
   contents.append(file_text)

   if file_text == file_finish:
      # close the file
      file.close()
      break

print(contents)
data = ' '.join([str(elem) for elem in contents])  
print(data)
file.write(data)
file.close()
file_name = input("Enter filename: ")

if len(file_name) == 0:
   print ("Next time please enter something")
   sys.exit()

try:
   file = open(file_name, "r")

except IOError:
   print ("There was an error reading file")
   sys.exit()
file_text = file.read()
file.close()
print (file_text)


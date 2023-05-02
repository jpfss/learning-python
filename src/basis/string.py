# -*- coding: utf-8 -*-
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

# =============================================================================
# Accessing Values in Strings
# =============================================================================
var1 = 'Hello World!'
var2 = "Python Programming"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

# =============================================================================
# Updating Strings
# =============================================================================
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')

# =============================================================================
# Escape Characters
# =============================================================================

# =============================================================================
# String Special Operators
# =============================================================================


# =============================================================================
# String Formatting Operator
# =============================================================================
print ("My name is %s and weight is %d kg!" % ('Zara', 21)) 

# =============================================================================
# Triple Quotes
# =============================================================================
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print ("paragram is: %s"%(para_str))
print ('C:\\nowhere')
print (r'C:\\nowhere')

# =============================================================================
# Unicode String
# =============================================================================

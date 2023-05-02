# -*- coding: utf-8 -*-
def printme(str):
   "This prints a passed string into this function"
   print (str)
   return

# =============================================================================
# Calling a Function
# =============================================================================
# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")
# =============================================================================
# Pass by Reference vs Value 
# =============================================================================
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function before change: ", mylist)
   
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

# =============================================================================
# Function Arguments
# =============================================================================
# Now you can call printme function
# 没定义，会报错
# printme()
printme( str = "My string")
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age = 50, name = "miki" )

# =============================================================================
# Default Arguments
# =============================================================================
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age = 50, name = "miki" )
printinfo( name = "miki" )

# =============================================================================
# Variable-length Arguments
# =============================================================================
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

# =============================================================================
# The Anonymous Functions
# =============================================================================
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

# =============================================================================
# The return Statement
# =============================================================================
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total

# Now you can call sum function
total = sum( 10, 20 )
print ("Outside the function : ", total )
# =============================================================================
# Scope of Variables
# =============================================================================

# =============================================================================
# Global vs. Local variables
# =============================================================================
total = 0   # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total

# Now you can call sum function
sum( 10, 20 )
print ("Outside the function global total : ", total )
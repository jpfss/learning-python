# -*- coding: utf-8 -*-

def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32


print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))

# =============================================================================
# try
# =============================================================================
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
# =============================================================================
# The try-finally Clause
# =============================================================================
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print("Error: can\'t find file or read data")
    fh.close()

try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can\'t find file or read data")
# =============================================================================
# Argument of an Exception
# =============================================================================
# Define a function here.


def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n", Argument)


# Call above function here.
temp_convert("xyz")
# =============================================================================
# Raising an Exception
# =============================================================================


def functionName(level):
    if level < 1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
    return level


def functionName(level):
    if level < 1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
    return level


try:
    l = functionName(-10)
    print("level = ", l)
except Exception as e:
    print("error in level argument", e.args[0])

# =============================================================================
# User-Defined Exceptions
# =============================================================================
try:
    raise Networkerror("Bad hostname")
except Networkerror, e:
    print e.args

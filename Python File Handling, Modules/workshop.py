# Python File Handling Lesson

# Python provides built-in functions to easily read, write, and manipulate files.

'''
    Reading Files:
    "read()" - Reads the entire content of the file
    "readline()" - Reads a single line
    "readlines()" - Reads all lines and returns a list
    
    Common Modes:
    "r" - Read (default)
    "w" - Write (overwrites the file)
    "a" - Append (adds to the file)
    "x" - Create (creates a new file, raises error if the file exists)
    "b" - Binary (used for binary files like images)
    "t" - Text (default)
'''


# 1. Open and read a .txt file
# NOTE: open() returns a file object.
file = open("workshop.txt", 'r')
print(file)
content = file.read()
print(content)
file.close()

# 2. Writing to a .txt file
# write(): writes a string to the file
file = open("workshop.txt", "w")
file.write("I am writing too the txt file from Python!")


# writelines(): writes a list of strings
file.writelines(["\nstudent1: Adam\n", "student2: Kyle\n", "student3: Victoria\n", "student4: Tony\n"])
file.close()

# 3. Appending to Files: Add content to an existing file
file = open('workshop.txt', 'a')
file.write("I am Allan the Instructor")
file.close()


# opening a file with the "with" statement: good practice and recommended way of opening files because it automatically closes the file
print("************** THIS IS FROM THE 'WITH' STATEMENT*******************")

with open("workshop.txt", 'r') as file:
    content = file.read()
    print(content)



# Python Modules Lesson: allows you to structure your code and reuse it in other programs. Its just a .py file containing python code (functions, classes, or variables)

# 1. Importing a module
import math
print(math.pi)



# 2. Creating your own Module
import mymodule
print(mymodule.greet("Tony"))

# Importing Specific Functions
from math import sqrt
result = sqrt(16)
print(result)
# Using "as" to Rename a Module or Function
import math as m
print(m.sqrt(16))

from math import pi as pie
print(pie)

# use the "." for nested imports
from all_modules import anotherone
print(anotherone.loop_students(['victoria', 'adam', 'tony', 'kyle']))

print("*********************************")

from all_modules.python_modules import finalemodule
print(finalemodule.loop_students(['victoria', 'adam', 'tony', 'kyle']))



# 3. Built-in and Third-Party Modules: Python has a large set of built-in modules (like "os", "sys", "datetime"). You can also install third-party modules using "pip or pip3"
import requests
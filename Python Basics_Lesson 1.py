# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 09:43:13 2021

@author: Arian

"""

print('Hello, Python!')
# Check the Python Version
import sys
print(sys.version)

# Practice on writing comments
print('Hello, Python!') # This line prints a string
#print('hi')

# Print string as error message
print('HELLO')
# Try to see built in error message
print('Hello, Python')

# Print string and error to see the running order
print('This will be printed')
print('This will cause an error') #error fixed
print('This will NOT be printed')

# Type of 12
print(type(12))
# Type of 2.14
print(type(2.14))
# Type of 'Hello, Python 101!'
print(type('Hello, Python 101!'))
#Type of 12.0
print(type(12.0))
#Type of -4
print(type(-4))
#System settings about float type
print(sys.float_info)

#Verify that this is an integer
print(type(2))
# Convert 2 to float
print(float(2))
print(type(float(2)))
#Casting 1.1 to integer will result in loss of information
print(int(1.1))
# Convert a string into an integer with error
print(int(1.2)) # Original code int('1 or 2 people') Error fixed
# Convert the string "1.2" into a float
print(float('1.2'))
# Convert an integer to a string
print(str(1))
# Convert a float to a string
print(str(1.2))

# Type of True
print(type(True))

# Type of False
print(type(False))

# Covert True to int
print(int(True))

#Convert False to int
print(int(False))

# Convert 1 to boolean
print(bool(1))

#Convert 0 to boolean
print(bool(0))

#Convert True to float
print(float(True)) 

# What is the data type of 6/2
print(type(6/2))

# Addition operation expressions
print(43+60+16+41)

# Subtraction operation expression
print(50-60)

# Multiplication operation expression
print(5*5)

#Division operation expression
print(25/5)

#Integer division operation expression
print(25//6)

# How many hours are in 160 min
print(160/60)

# Store value into variable
x=43+60+16+41
# Print out the value in variable
print(float(x))

# Use another variable to store the result of the operation between variable and value
y=x/60
print(int(y))

# Overwrite variable with new value
x=x/60
print (x)

# Name the variables meaningfully
total_min= 43+42+57 # Total length of albums in minutes
print(total_min)
total_hours= total_min/60 # Total length of albums in hours
print(total_hours)






















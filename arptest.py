#!/user/bin/env python

''' 

    This is my doc string

'''

try:
    raw_input
except NameError:
    raw_input = input

myinput = raw_input('prompt me:')
print(myinput)

# IMPORT
import hello
import math  # modules from Python Standard Library
import matplotlib  # external modules (via pip install)
from random import randint  # specific import
import math as m  # aliasing modules

# import own module from the same dir
import own_module
# import own module from another dir
# 1. using sys module for set the path of the own module
import sys
sys.path.append('/path/modules')
# 2. add the module to the path where Python checks for modules
# and packages. This is a more permanent solution that makes the
# module available environment-wide or system-wide,
# making this method more portable.
print(sys.path)  # move your module.py file into that directory

# EXPORT (own modules)
# nothing special

# List module identificators
print(dir(mymodule))

'''If some code not need to be executed in importing file, get some
restrictions. If the program is being imported from
another program, then __name__ would be set to the module's name.
'''


def sum1(a, b):
    c = a+b
    return c


if __name__ == '__main__':
    print("Sum is ", sum1(3, 6))


# PACKAGE
'''
Python modules is a single file, whereas a Python package is a directory
that contains Python modules and one additional file: __init__.py.
The file can also be used to import the module, so we can
from package import * 
'''

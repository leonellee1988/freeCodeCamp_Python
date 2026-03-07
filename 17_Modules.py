import math

print(math.sqrt(36))

# We might want to import just some of the elements of the module

from math import radians, sin, cos

# Now we can call these functions directly, without the module name as a prefix

# Other hand, we might want to get all elements of the module

from math import *

# A very important thing to know:

if __name__ == '__main__':
    pass

"""
__name__ is a special built-in variable in Python.

When a Python file is executed directly, Python sets the value of this variable to the string "__main__".

But if the Python file is imported as a module into another Python script, the value of the __name__ variable is set 
to the name of that module (usually the filename without the .py extension).

This is why you'll often find this conditional in Python scripts. It contains the code that you want to run only if 
the Python script is running as the main program:

if __name__ == '__main__': 
    # Code

But if the script is imported as a module, the code within that block doesn't run.

This is helpful because it allows Python scripts to have two purposes. They can be run directly 
to execute their main logic, or they can be imported into another module without executing their main logic.
"""
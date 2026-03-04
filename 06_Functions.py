# Functions

def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(10, 30)
print(my_sum)

def greeting(name):
    return f'Hello {name}, good morning and a wonderful week!'

my_greeting = greeting('Edwin Lee')
print(my_greeting)

"""
Note:

Python follows the LEGB rule, which stands for the following:

1. Local scope: Variables defined in functions or classes
2. Enclosing scope: Variables defined  in enclosing or nested functions
3. Global scope: Variables defined at the top level of the module or file
4. Built-in scope: Reserved names in Python for predefined functions, modules, keywords and objects
"""

# Local scope:

def my_func():
    my_var = 'Hello'
    print(my_var)

# print(my_var) NameError: name 'my_var' is not defined

my_func()

# Enclosing scope:

def outer_func():
    msg = 'Hello there!'
    def inner_func():
        print(msg)
    inner_func()

outer_func()

# Note: inner_func can access the msg, but outer_func cannot access variables defined within inner_func

def outer_func_1():
    msg = 'Hello there!'
    res = ''
    print(msg)
    def inner_func():
        nonlocal res
        res = 'Hi, how you doing?'
        print(res)
    inner_func()

outer_func_1()

# Global scope:

my_var = 100

def show_var():
    print(my_var)

show_var()

# If we want to make a locally scoped variable defined inside a function globally accessible, we use 'global'

def show_var_1():
    global my_var_2
    my_var_2 = 200
    print(my_var, my_var_2)

show_var_1()
print(my_var_2)
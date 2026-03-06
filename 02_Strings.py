# Multi-line string

my_str_1 = """Multiline
string
"""

my_str_2 = '''Multiline
string
'''
print(my_str_1)
print(my_str_2)

# How to use simple quotes within double quotes, and vice versa

msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
print(msg, quote)

# The "in" operator

my_str_3 = "Hello world"

print("Hello" in my_str_3)
print("hey" in my_str_3)
print("hi" in my_str_3)
print("e" in my_str_3)

# The "len" built-in function

print(len(my_str_3))

# Index of a character

print(my_str_3[0])
print(my_str_3[-1])

# IMPORTANT: strings are inmutable data types in Python. This means that you can reassing a different string to a variable

greeting = 'Hello'
greeting = 'Hi'
print(greeting)

# String interpolation

name = 'Linux Torvalds'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age)

# String slicing

print(my_str_3[1:4])
print(my_str_3[:7])
print(my_str_3[8:])
print(my_str_3[0:11:2])
print(my_str_3[::-1]) #dlrow olleH

# Built-in methods for working with strings

print(my_str_3.upper())
print(my_str_3.lower())

my_str_4 = '          Hello world!          '
print(my_str_3.strip())

print(my_str_3.replace('Hello', 'Hi'))
print(my_str_3.split())

my_list = ['Hello', 'world!', 'Im', 'learning', 'Python']
print(' '.join(my_list))

print(my_str_3.startswith('Hello'))
print(my_str_3.endswith('world'))
print(my_str_3.find('world'))
print(my_str_3.count('o'))
print(my_str_3.title())

# The built-in 'str.maketrans()' method:

lower_chars = 'abc'
upper_chars = 'ABC'
table = str.maketrans(lower_chars, upper_chars)
print(table)

# Built-in 'split()' method

phrase = 'Hello Word, we area learning Python'
words = phrase.split(" ")
print(words)

# Note: very important to notice that the method create a list (not need to add 'list()')
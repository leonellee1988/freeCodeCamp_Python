# Interactive Debugging with 'pdb' module

import pdb

def divide(a, b):
    pdb.set_trace()
    return a/b

print(divide(10, 2))
print(divide(15, 3))

# Handling Work

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero")

try:
    number = int(input("Give me a number: "))
except ValueError as error:
    print(f"{error}")
else:
    try:
        x = 10 / number
    except ZeroDivisionError as error:
        print(f"{error}")
    else:
        print(x)
    finally:
        print("This block always run!")

# Or we can do a shorter version

try:
    number1 = int(input("Enter an integer number: "))
    number2 = int(input("Enter another number: "))
    result = number1 / number2
except (ValueError, ZeroDivisionError) as error:
    print(f" Error occurred: {error}")

# The 'raise' statement

def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as error:
    print(f'Error: {error}')

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise # If I comment this line, I won't see the next 'print'

try:
    process_data('hello')
except ValueError:
    print('Handle at higher level')

def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative numbers'
    return number ** 0.5

try:
    print(calculate_square_root(-4))
except ValueError as error:
    print(f'Assertion failed: {error}')
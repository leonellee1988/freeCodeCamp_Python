# Falsy and truthy values

print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))

print(bool(1))
print(bool("Hello"))

# Boolean operators

is_citizen = True
age = 25
print(is_citizen and age)

# No nested if statements:

if is_citizen:
    if age >= 18:
        print('You are eligible to vote')
    else:
        print('You are not eligible to vote')

if is_citizen and age >= 18:
    print('You are elegible to vote')
else:
    print('You are not elegibl to vote')

# Note: In Python, if conditions don't have to compare values explicity True of False.

is_member = True
discount = 0

if is_member:
    discount = 3
    print(f'User qualifies for membership discount: {discount}')
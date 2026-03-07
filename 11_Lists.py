# list() constructor

developer = 'Edwin'
my_list_1 = list(developer)
print(my_list_1)


# Note: remember, lists are mutable: you can update any element in the list

programming_languages = ['Python', 'Javascript', 'C++', 'Rust']
programming_languages[1] = 'Java'
print(programming_languages)

# Keyword 'del' for remove an element in a list

del programming_languages[3]
print(programming_languages)

# Keyword 'in' for check if an element is in a list

print('Pascal' in programming_languages)

# Nested lists

developer_2 = ['Edwin', 38, 'Antigua Guatemala', ['Python', 'Javascript', 'Java']]
print(developer_2[3][0])

# Unpacking values from lists

name, age, adress, languages = developer_2
print(name, age, adress, languages)

name, *rest = developer_2
print(rest)

# Slicing

personal_info = developer_2[0:3]
print(personal_info)

my_list_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(my_list_2[1::2])

# Methods used for lists

# append()

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

other_numbers = [7,8,9,10]
numbers.append(other_numbers)
print(numbers)

# extend()

my_list_3 = [1,2,3,4,5]
my_list_4 = [6,7,8,9,10]
my_list_3.extend(my_list_4)
print(my_list_3)

# insert()

my_list_3.insert(10, 11)
print(my_list_3)

# remove()

my_list_3.remove(11)
print(my_list_3)

# Note: This method only remove the first occurrence of an item

my_list_5 = [10, 10, 20, 20, 20, 30, 30, 30 ,30]
my_list_5.remove(30)
print(my_list_5)

# pop()

erased_num = my_list_3.pop(9)
print(my_list_3)
print(erased_num)

# clear()

my_list_5.clear()
print(my_list_5)

falsy_list = [0,1,2,3,4,5]
print(all(falsy_list))

# sort()

numbers_2 = [12, 39, 1, -20, 100, 57]
numbers_2.sort()
print(numbers_2)

# Note: we can also use the built-in function 'sorted'

sorted_numbers = sorted(numbers_2)
print(sorted_numbers)

# reverse()

sorted_numbers.reverse()
print(sorted_numbers)

# index()

print(programming_languages.index('C++'))

# The built-in 'all()'

truthy_list = [1,2,3,4,5]
print(all(truthy_list))

falsy_list = [0,1,2,3,4,5]
print(all(falsy_list))
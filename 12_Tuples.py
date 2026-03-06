# Tuples are similar to list, but while lists are mutable data type, tuples are inmutable

# tuple() constructor

developer = "Edwin Lee"
my_tuple = tuple(developer)
print(my_tuple)

"""
So when might you use a tuple over a list?

If you need a dynamic collection of elements where you can add, remove and udpate elements,
then you should use a list. If you know that you are working with a fixed and inmutable collection
of data, then you should use a tuple
"""

# Methods for working with tuples

# count()

programing_languages = ('Python', 'Javascript', 'Java', 'Python', 'C++', 'Turbo Pascal', 'Python')
print(programing_languages.count('Python'))

# index()

print(programing_languages.index('Python', 4))

# Built-in function 'sorted'

numbers = (100, -15, 57, 29, 38, -126)
sorted_numbers = sorted(numbers) #it will be a list
print(sorted_numbers)

sorted_languages = sorted(programing_languages, key=len) # again, it will be a list
print(sorted_languages)

reversed_numbers = sorted(numbers, reverse=True)
print(reversed_numbers)
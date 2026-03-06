# Loop 'for'

programming_languages = ['Python', 'Java', 'Javascript', 'C++', 'Turbo Pascal']

for language in programming_languages:
    print(language)

categories = ['Fruit', 'Vegetables']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

# Loop 'while'

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again')
print('You got it!')

# 'break' statement

programming_languages = ['Python', 'Java', 'Javascript', 'C++', 'Turbo Pascal']

for language in programming_languages:
    if language == 'C++':
        break
    print(language)

for language in programming_languages:
    if language == 'C++':
        continue
    print(language)

# Using 'else' clause with loops

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'{word} contains the vowel {letter}')
            break
    else:
        print(f'{word} does not have vowels')

# The 'range(start, stop, step)' function

for n in range(2, 20, 2):
    print(n)

for n in range(50, 0, -5):
    print(n)

my_list = list(range(1, 11))
print(my_list)

# The 'enumerate()' function

languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages)))

for index, language in enumerate(languages):
    print(index, language)

# Note: We can add a 'start' argument that specifies the starting value for the count

for index, language in enumerate(languages, 1):
    print(index, language)

# Built-in 'zip()' function

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(ids, developers)))

for id, developer in zip(ids, developers):
    print(id, developer)

# List Comprehensions

even_numbers = [num for num in range(0, 21) if num % 2 == 0]
print(even_numbers)

numbers = list(range(0, 21))
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

# Built-in 'filter()' function: accepts a function and an iterable for its arguments

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4 # The function returns a boolean

long_words = list(filter(is_long_word, words))
print(long_words)

def is_even(num):
    return num % 2 == 0

even_list = list(filter(is_even, numbers))
print(even_list)

# The 'map()' function: takes an iterable and applies a function to each of its elements

def to_odd(num):
    return num + 1

odd_list = list(map(to_odd, even_list))
print(odd_list)

# The 'sum()' function:

numbers_1 = [1, 3, 5, 7, 11]
print(sum(numbers_1))

print(sum(numbers_1, start=10)) # this add the 10 to the sum

# Lambda functions

"""
When we work with higher order functions like 'map()' or 'filter()', we can use an anonymous
inline function: the lambda function
"""

numbers_2 = list(range(0, 21))
even_list_2 = list(filter(lambda num:num % 2 == 0, numbers_2))
print(even_list_2)

square_list = list(map(lambda num: num**2, numbers_2))
print(square_list)
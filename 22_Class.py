class ClassName:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sample_method(self):
        print(self.name.upper())

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name.upper()} says woof woof")

# Let's create two dogs using the 'Dog' class as the blueprint

dog_1 = Dog('Lucas', 5)
dog_2 = Dog('Laika', 3)

# How to see the attributes of our dogs

print(dog_1.name, dog_1.age)
print(dog_2.name, dog_2.age)

# We can call the 'bark' method

dog_1.bark()
dog_2.bark()

# Attributes are variables that belong to an object, so they hold data

# There are two kinds of attribues:

# 1. Instance attributes are unique to each object and we usually set them with the '__init__'
# 2. Class attributes belong to the class itself and are shared by all instances of the class

class Dog:
    species = 'French Bulldog'

    def __init__(self, name):
        self.name = name

print(Dog.species)
dog_3 = Dog('Spike')
print(dog_3.species)
print(dog_3.name)

# Methods are functions defined inside a class

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def describe(self):
        return f"This car is a {self.color} {self.model}"

car_1 = Car('Orange', 'Hyundai')
print(car_1.describe())

# Dunder methods ('d' for double and 'under' for underscores)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"
    
    def __eq__(self, other):
        return self.pages == other.pages
    
book_1 = Book("Built Wealth Like a Boss", 420)
book_2 = Book("Be Your Own Start", 420)

print(len(book_1))
print(len(book_2))
print(str(book_1))
print(str(book_2))
print(book_1 == book_2)

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"'{item}' is not in cart")
    
    def list_items(self):
        return self.items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self, item):
        return item in self.items
    
    def __iter__(self):
        return iter(self.items) #This function allows me to iterate over the items in the 'cart' object
    
cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
    print(item)

print(cart.list_items())
print(len(cart))
print(cart[3]) #__getitem__
print("Monitor" in cart)#__contains__

# Handle object attributes dynamically

# Python gives you four built-in functions to dynamically work with objects attributes:

# getattr() - getattr(object, attribute_name, default_value)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Bebay Hernández', 35)
print(getattr(person, 'name'))

# attr_name = input('Enter the attribute you want to see: ')
# print(getattr(person, attr_name, 'Attribute not found'))

for attr in dir(person):
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f'{attr}: {value}')

class Student:
    def __init__(self, id, name, lastname, faculty):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.faculty = faculty

student = Student(1, 'Edwin', 'Lee', 'Math')

for attr in dir(student):
    value = getattr(student, attr)
    print(f"{attr}: {value}")

# setattr() - setattr(object, attribute_name, value)

class Configuration:
    pass

# Data loaded at runtime

settings_data = {
    'server_url': 'https://api.example.com',
    'time_sec': 30,
    'max_retries': 5
}

config_object = Configuration()

#Dynamically set attributes using dictionary keys and values

for attr_name, attr_value in settings_data.items():
    setattr(config_object, attr_name, attr_value)

print(config_object.server_url)
print(config_object.time_sec)
print(config_object.max_retries) 

class Worker:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department

worker = Worker(1, 'Bruce Lee', 'Science' )

benefits_science_dep = {
    'salaries_per_year': 14,
    'hours_per_day': 6,
    'vacation_per_year': 30
}

for attr_name, attr_value in benefits_science_dep.items():
    setattr(worker, attr_name, attr_value)

for attr in dir(worker):
    value = getattr(worker, attr)
    print(f'{attr}: {value}')

# But if we just want or need to see an attribute in specific:

worker_attribute = input('Enter the attribute you want to see from the worker: ')

print(getattr(worker, worker_attribute, 'Attribute not found'))

# hasattr() - hasattr(object, attribute_name)

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

book_1 = Book('The Alchemist', 'Paulo Coelho', 200)

required_attributes = ['name', 'author', 'pages', 'price']

for attr in required_attributes:
    if not hasattr(book_1, attr):
        print(f'Error, book is missing the required attribute: {attr}')
    else:
        print(f'{attr}: {getattr(book_1, attr)}')

# delattr - delattr(object, attribute_name)

class Movie:
    def __init__(self, name, category, year, duration):
        self.name = name
        self.category = category
        self.year = year
        self.duration = duration
        self.temp_comment = 'It is my favorite movie of all time'
        self.temp_earnings = 100

movie = Movie('V for Vendetta', 'Comics', 2010, '1 hour and 30 minutes')

attributes_to_clean = ['temp_comment', 'temp_earnings']

for attr in attributes_to_clean:
    if hasattr(movie, attr):
        delattr(movie, attr)
        print(f'Removed attribute: {attr}')

for attr in dir(movie):
    if not attr.startswith('__') and not callable(getattr(movie, attr)):
        print(f'{attr}: {getattr(movie,attr)}')
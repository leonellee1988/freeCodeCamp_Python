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

class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
student1 = Student('std-0001', 'Bebay Hernández', 35)

#stu_attr = input('Enter the attribute you want to see: ')
#print(getattr(student1, stu_attr, "Attribute not found"))

#If we want to see all the attributes for our object:

for attr in dir(student1):
    if not attr.startswith('__') and not callable(getattr(student1, attr)):
        value = getattr(student1, attr)
        print(f"{attr}: {value}")

# setattr() - setattr(object, attribute_name, value)

class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_object = Configuration()

for attr_name, attr_value in settings_data.items():
    #print(attr_name, attr_value)
    setattr(config_object, attr_name, attr_value)

print(config_object.server_url)
print(config_object.timeout_sec)
print(config_object.max_retries)

# hasattr - hasattr(object, atribute_name)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_1 = Product("T-Shirt", 25)

required_attributes = ["name", "price", "inventory_id"]

for attr in required_attributes:
    if not hasattr(product_1, attr):
        print(f"Error: Product is missing the required attribute: {attr}")
    else:
        print(f"'{attr}': {getattr(product_1, attr)}")

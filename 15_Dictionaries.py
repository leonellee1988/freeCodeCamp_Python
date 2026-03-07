# Dictionaries

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

print(pizza)

# The 'dict()' constructor

pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
print(pizza)

# Access to dictionaries elements

print(pizza['price'])

# Update a dictionary value

pizza['price'] = 10
print(pizza)

# Methods for work with dictionaries

# .get(key, default)

print(pizza.get('name', 'Not found'))
print(pizza.get('size', 'Not found'))

# .keys() and .values() methods

print(pizza.keys())
print(pizza.values())

# .items() 

print(pizza.items())

# The .clear() method removes all the key-value pairs from the dictionary

# pop()

pizza.pop('toppings')
print(pizza)

pizza.popitem() # removes the last key-value pair
print(pizza)

# .update()

pizza.update({
    'size': 'Big',
    'delivery': True
})
print(pizza)

# Loop over dictionaries

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250, 
    'Headphones': 70
}

for product in products.keys():
    print(product)

for price in products.values():
    print(price)

# What if we want to set a discount of 20% in all our prices

for product, price in products.items():
    print(products[product])
    products[product] = round(price*0.80)

print(products)

for product in enumerate(products):
    print(product)

for price in enumerate(products.values()):
    print(price)

for index, price in enumerate(products.values()):
    print(index, price)
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.temp_price = 1
        self.temp_stock = 1

# Specific attributes for electronic products

electronic_attributes = {
    'warranty_months': 12,
    'power_watts': 120,
    'requires_battery': False
} 

# Required attributes for electronic products

required_attributes = ['id', 'name', 'price', 'stock', 'warranty_months', 'power_watts', 'requires_battery', 'colour']

# Temporarily attribute to clean

attribute_to_clean = ['temp_price', 'temp_stock']

# Product catalogue:

prod_1 = Product('P-001', 'A4 Notebook', 2.50, 120)
prod_2 = Product('P-002', 'HB Pencil', 0.30, 500)
prod_3 = Product('P-003', 'Smartphone X', 699.99, 25)
prod_4 = Product('P-004', 'Wi-Fi Router', 49.90, 40)
prod_5 = Product('P-005', 'School Backpack', 39.99, 80)

# Set the specific attributes for electric products:

for attr_name, attr_value in electronic_attributes.items():
    setattr(prod_3, attr_name, attr_value)

# Get all attributes for 'product_3':

for attr in dir(prod_3):
    if not attr.startswith('__') and not callable (getattr(prod_3, attr)):
        value = getattr(prod_3, attr)
        print(f'{attr}: {value}')

# Look for required attributes for 'product_3'

for attr in required_attributes:
    if not hasattr(prod_3, attr):
        print(f'Error, the product is missing the required attribute: {attr}')
    else:
        print(f'{attr}: {getattr(prod_3, attr)}')

# Delete temporarily attributes

for attr in attribute_to_clean:
    if hasattr(prod_3, attr):
        delattr(prod_3, attr)
        print(f'Removed attribute: {attr}')

for attr in dir(prod_3):
    if not attr.startswith('__') and not callable(getattr(prod_3, attr)):
        print(f'{attr}: {getattr(prod_3, attr)}')
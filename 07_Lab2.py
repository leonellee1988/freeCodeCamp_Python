# Build a discount calculator

def apply_discount(price, discount):
    if not (isinstance(price, int) or isinstance(price, float)):
        return 'The price should be a number'
    elif not(isinstance(discount, int) or isinstance(discount, float)):
        return 'The discount should be a number'
    elif price <= 0:
        return 'The price should be greater than 0'
    elif discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    else:
        discount /= 100
        price = price - (price * discount)
        return price

print(apply_discount(100, 70))
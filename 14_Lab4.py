# Build a Number Pattern Generator

def number_pattern(n):
    list_num = []
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    for num in range(1, n + 1, 1):
        list_num.append(str(num))
    return ' '.join(list_num)
    
print(number_pattern(5))
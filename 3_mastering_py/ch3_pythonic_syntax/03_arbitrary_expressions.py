username = 'wolph'
a = 123
b = 456
some_dict = dict(a=a, b=b)

print(f'a: {some_dict["a"]}')
print(f'sum: {some_dict["a"] + some_dict["b"]}')

## python expressions, specifially an inline if statement
print(f'if statement: {a if a > b else b}')

## function calls
print(f'min: {min(a, b)}')

print(f'Hi {username}. and in uppercase {username.upper()}')

## loops
print(f'squares: {[x ** 2 for x in range(5)]}')

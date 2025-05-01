n = 39
remainders = []

while n > 0:
    # returns a tuple with the result of the integer division and its remainder
    # For example, divmod(13, 5) would return (2, 3)
    n, remainder = divmod(n, 2)
    remainders.append(remainder)
remainders = remainders[::-1]
print('remainders:', remainders)

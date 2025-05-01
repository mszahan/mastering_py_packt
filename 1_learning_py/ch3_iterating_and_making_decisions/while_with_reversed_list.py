n = 39
remainders = []

while n > 0:
    reminder = n % 2
    remainders.append(reminder)
    # n = n // 2 the follwining line is equivalent
    n //= 2
# this reverses the list in place
remainders = remainders[::-1]
print('remainders:', remainders)

num = 35
# it returns the integer division of the number
print(35 // 2)
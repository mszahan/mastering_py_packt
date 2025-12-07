# the dense code is not as readable
f = lambda x: 0**x or x*f(x-1)
print(f(5))


# the sparse code is better
def factorial(x):
    if 0 ** x:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(10))

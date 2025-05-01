from itertools import compress
data = range(10)
even_selector = [1, 0]*10
odd_selector = [0, 1]*10
# compress('ABC', (1, 0, 1)) would give back 'A' and 'C', 
# because they correspond to the 1's
# dd_selector and even_selector are 20 elements long,..... 
# while data is just 10 elements long. compress will stop as soon as...
# data has yielded its last element
even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print('Odd selectors:', odd_selector)
print('Even selectors:', even_selector)
print('list of Data:', list(data))
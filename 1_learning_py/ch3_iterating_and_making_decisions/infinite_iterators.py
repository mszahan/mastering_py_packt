from itertools import count
# it gives you sequence of numbers starting from the first argument
# and incrementing by the second argument
# count(start, step)
for n in count(5,3):
    if n > 20:
        break
    print(n, end=', ')

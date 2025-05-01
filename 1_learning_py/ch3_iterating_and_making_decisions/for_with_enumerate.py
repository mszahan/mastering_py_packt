surnames = ['Smith', 'Jones', 'Taylor', 'Brown', 'Williams']
# enumerate gives back a 2-tuple (position, surname)
# much more readable (and more efficient) than the range(len(...))
for index, surname in enumerate(surnames):
    print(index, surname)

n = 5
squared_numbers = [x ** 2 for x in range(n+1)]
print('list comp.', squared_numbers)

zeros = [0 for _ in range(5)]
print('zeros', zeros)

# dictionary comprehension
my_string = 'Fifa worldcup'
nb_occurences = {letter: 0 for letter in my_string}
print(nb_occurences)


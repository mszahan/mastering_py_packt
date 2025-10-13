name = 'Rick'

print('Hi %s' %name)
print('Hi {}'.format(name))
print(f'Hi {name}')

value = 1 / 3
print('the value is %.3f' %value)
print('the value is {:.2f}'.format(value))


print('Hi {0}, value: {1:.3f}. By {0}'.format(name, value))
print(f'Hi {name}, the value is {value:.2f}')
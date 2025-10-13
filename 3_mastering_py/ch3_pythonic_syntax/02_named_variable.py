name = 'Rick'

print('Hi %(name)s' % dict(name=name))
print('Hi {name}'.format(name=name))
print(f'Hi {name}')

#the nested code is not as readable
def between_and_modulo(value, a, b, modulo):
    if value >=a:
        if value <= b:
            if value % modulo:
                return True
    return False


for i in range(10):
    if between_and_modulo(i, 2, 9, 2):
        print(i, end=' ')

# this is the flat code which is better
def between_and_modulo_flat(value, a, b, modulo):
    if value < a:
        return False
    elif value > b:
        return False
    elif value % modulo:
        return False
    else:
        return True

for i in range(10):
    if between_and_modulo_flat(i, 2, 9, 2):
        print(i, end=' ')

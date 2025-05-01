def outer():
    test = 1

    def inner():
        test = 2
        print(f"Inner: {test}")
    inner()
    print(f"Outer: {test}")
test = 0
outer()
print(f"Global: {test}")
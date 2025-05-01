class DriverException(Exception):
    pass

people = [('John', 25), ('Jane', 30), ('Doe', 35)]
driver = None

# for person, age in people:
#     if age >= 36:
#         driver = (person, age)
#         break

# if driver is None:
#     raise DriverException("No driver found")

# we can write the above code using else with for loop
# it will work in while loop too
for person, age in people:
    if age >= 36:
        driver = (person, age)
        break
else:
    raise DriverException("No driver found")
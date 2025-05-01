people = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
nationalities = ['USA', 'UK', 'Canada']
for person, age in zip(people, ages):
    print(f"{person} is {age} years old.")

# explicitly unpacking the tuple
for person, age, nationality in zip(people, ages, nationalities):
    print(f"{person} is {age} years old and from {nationality}.")

# implicitly unpacking the tuple
for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(f"{person} is {age} years old and from {nationality}.")
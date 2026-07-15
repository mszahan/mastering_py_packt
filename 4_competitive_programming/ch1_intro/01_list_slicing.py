list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# the 2nd element of the list
second_element = list_of_numbers[1]
print('second number of the list:', second_element)

# the list of elements between 2nd and 5th elements
middle_of_list = list_of_numbers[2:5]
print('Middle of the list elements', middle_of_list)

# the first j elements L[:j]
first_elements = list_of_numbers[:5]
print('first 5 elements of the list', first_elements)

#all elements from the ith onwards L[i:]
last_elements = list_of_numbers[4:]
print('last elements from position 5th', last_elements)

# the last 3 elements of list L[-3:]
last_three = list_of_numbers[-3:]
print('last three elements:', last_three)

# elements from the ith upto (but not including) the jth,
# taking every kth element L[i:j:k]
interval_slice = list_of_numbers[2:7:2]
print('Interval slicing of the list elements: ', interval_slice)

# the elements of list with even indices L[::2]
even_indices = list_of_numbers[::2]
print('Even indices: ', even_indices)

# a reverse copy of the list
reverse_copy = list_of_numbers[::-1]
print('Reverse copy of the list: ', reverse_copy)
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# length of list - O(1)
length = len(list_of_numbers)
print('length of list:', length)

# return a sorted copy of list - O(n log n)
sorted_list = sorted(list_of_numbers)
print('Sorted list: ', sorted_list)

# sorts list in place - O(n log n)
print('sorted in place:', list_of_numbers.sort())

# the number of occurence of element in list - O(n)
number_of_tow_in_list = list_of_numbers.count(2)
print('number of 2 occurs in the list: ', number_of_tow_in_list)

# if element found in the list - O(n)
print('If 2 present in the list:', 2 in list_of_numbers )

#appending new elements at the end of list  - amortised O(1)
new_list = list_of_numbers.append(5)
print('new list of numbers: ', new_list)

#return the last element of the list - amortised O(1)
before_pop = list_of_numbers
poped_nuber = list_of_numbers.pop()
print(f'Befor popped list: {before_pop} \n \
      Last pop number is {poped_nuber} \n \
      and the remaining list is: {list_of_numbers}')
A = [1, 2, 3]

# this is not the copy
# Both A and B refers to the same object
# Changing A will also affect not_copy

not_copy = A

# this is actula copy
# now changing the value of A will not affect actual_copy
actual_copy = A[:]
reverse_copy = A[::-1]
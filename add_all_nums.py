# Write a function that takes in a list of numbers. It should return the sum of all the numbers in the list.

# For example:

# [1, 1, 1] => 3

# [] => 0

def add_all_nums(numbers):
    # stores the value as you loop through list of numbers
    final_number = 0
    # for each number in the list, add given number to stored value (i)
    for num in numbers:   
        final_number += num
    # return i to get the final value
    return final_number 

print(add_all_nums([1, 2, 3]))
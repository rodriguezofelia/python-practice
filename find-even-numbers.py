#Write a function that takes in a list of numbers. It should return the indices of the even numbers.

# For example:

# [2, 5, 3, 4] => [0, 3]

# [1, 3, 5] => []

# [0, 2, 4, 6] => [0, 1, 2, 3]


def index_even_number(numbers):
    #empty list to add the index of the even numbers
    position = []

    for num in numbers: 
        #for each num that is divisble by 2
        if num % 2 == 0: 
            # add the index of the numbers that are even to the empty list
            position.append(numbers.index(num))
    return position



print(index_even_number([2, 5, 3, 4]))


# Solving with range 

def index_even_number(numbers):
    #empty list to add the index of the even numbers
    position = []
    # need the length of list to use range
    # range acts as a list of numbers to use as indices in our list
    for i in range(len(numbers)):
        # finds the num that is divisble by 2 at that given index
        if numbers[i] % 2 == 0: 
            # appends the index of that num to empty list
            position.append(i)
    return position

print(index_even_number([0, 2, 4, 6]))


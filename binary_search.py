"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    start = 0
    end = len(input_array)-1
    m = (end-start)/2
    while start <= end:
        if input_array[m] == value:
            return m
        elif input_array[m] > value:
            end = m - 1
            m = (end-start)/2
        elif input_array[m] < value:
            start = m + 1
            m = (end-start)/2 + start

    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
test_val3 = 1
test_val4 = 9
test_val5 = 0
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, test_val3)
print binary_search(test_list, test_val4)
print binary_search(test_list, test_val5)
#!python

def linear_search(array, item):
    """
    return the first index of item in array or None if item is not found
    works for sorted arrays
    """
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    position = 0
    found = False 

    while position < len(array) and not found:
        if array[position] == item:
            found = True
        else:
            if array[position] > item:
                stopped = True
            else: 
                position += 1

    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index == len(array):
        return None

    if array[index] == item:
        return item
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left_bound = 0
    right_bound = len(array) - 1

    found = False 

    while left_bound <= right_bound and not found:
        middle_value = (left_bound + right_bound) / 2)

        if array[middle_value]

        if array[middle_value] == item:
            found = True
        else: 
            if item < array[mid]:
                right_bound = mid-1
            else:
                left_bound = mid + 1
    return found
    
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if len(array) == 0:
        return False
    else:
        mid = len(array)/2

        if array[mid] == item:
            return True
        else:
            if item < array[mid]:
                return binary_search_recursive(array[:mid], item)
            else:
                return binary_search_recursive(array[mid+1:], item)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
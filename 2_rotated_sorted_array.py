def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if not input_list:
        return -1

    if len(input_list) == 1:
        return 0 if input_list[0] == number else -1

    pivot = find_pivot(input_list)

    # if target is greater than or equal to first element of input list, target must be left of the pivot
    if number >= input_list[0]:
        return binary_search(0, pivot, input_list, number)
    # target is smaller than the first element, so target must be right of the pivot
    return binary_search(pivot + 1, len(input_list) - 1, input_list, number)


def find_pivot(input_list):
    start_index = 0
    end_index = len(input_list) - 1
    mid_index = 0

    while start_index <= end_index:
        mid_index = (end_index + start_index) // 2

        if input_list[mid_index] > input_list[mid_index + 1]:
            return mid_index

        # array from start_index to mid_index is in order, so search in right half
        if input_list[start_index] < input_list[mid_index]:
            start_index = mid_index + 1

        # we've hit a rotated portion of the array.
        # coninue to search in the left half to find the pivot
        else:
            end_index = mid_index - 1

    return mid_index


def binary_search(start_index, end_index, input_list, target):
    mid_index = (end_index + start_index) // 2

    if end_index < start_index:
        return -1

    if input_list[mid_index] == target:
        return mid_index

    if input_list[mid_index] < target:
        return binary_search(mid_index + 1, end_index, input_list, target)
    return binary_search(start_index, mid_index - 1, input_list, target)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[], 6])
test_function([[2], 2])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

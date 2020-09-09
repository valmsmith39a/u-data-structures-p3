def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if not input_list:
        return [0, 0]

    if len(input_list) == 1:
        return [input_list[0], 0]

    quicksort(input_list)

    mid_index = len(input_list) // 2
    sublist_1 = [None for x in range(mid_index)]
    sublist_2 = [None for x in range(len(input_list) - mid_index)]

    index = 0
    index_1 = len(sublist_1) - 1
    index_2 = len(sublist_2) - 1

    while index < len(input_list):
        if (index == 0):
            sublist_2[index_2] = input_list[index]
            index_2 -= 1
            index += 1

        if sublist_1[index_1] == None:
            sublist_1[index_1] = input_list[index]
            index_1 -= 1
            index += 1

        if sublist_2[index_2] == None:
            sublist_2[index_2] = input_list[index]
            index_2 -= 1
            index += 1

    num1 = int("".join(map(str, sublist_1)))
    num2 = int("".join(map(str, sublist_2)))

    return [num1, num2]


def partition(items, begin_index, end_index):
    left_index = 0
    pivot_index = end_index

    while left_index != pivot_index:

        if items[left_index] < items[pivot_index]:
            left_index += 1
            continue
        # store left index item
        # move item at pivot_index - 1 to left index
        # move pivot item to pivot_index - 1
        # move left index item to pivot_index
        # update pivot_index
        item = items[left_index]
        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = items[pivot_index]
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index


def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = partition(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def quicksort(items):
    sort_all(items, 0, len(items) - 1)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[1, 2, 3, 4, 5], [542, 31]]
test_case_2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case_3 = [[], [0, 0]]
test_case_4 = [[2], [2, 0]]
test_case_5 = [[1, 2], [2, 1]]

test_function(test_case_1)
test_function(test_case_2)
test_function(test_case_3)
test_function(test_case_4)
test_function(test_case_5)

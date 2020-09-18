import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return ()

    if len(ints) == 1:
        return (ints[0], ints[0])

    min = ints[0]
    max = ints[0]

    for x in ints:
        if x < min:
            min = x

        if x > max:
            max = x

    return (min, max)

# Example Test Case of Ten Integers


l_ten = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l_ten)
print("Pass" if ((0, 9) == get_min_max(l_ten)) else "Fail")

l_hundred = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l_hundred)
print("Pass" if ((0, 99) == get_min_max(l_hundred)) else "Fail")

l_thousand = [i for i in range(0, 1000)]  # a list containing 0 - 9
random.shuffle(l_thousand)
print("Pass" if ((0, 999) == get_min_max(l_thousand)) else "Fail")

empty_list = []
print("Pass" if (() == get_min_max(empty_list)) else "Fail")

single_input_list = [1]
print("Pass" if ((1, 1) == get_min_max(single_input_list)) else "Fail")

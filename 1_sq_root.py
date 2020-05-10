def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start_index = 0
    end_index = number
    mid_index = 0

    while start_index <= end_index:

        mid_index = (end_index + start_index) // 2

        square = mid_index * mid_index

        if square == number:
            return mid_index

        elif square < number:
            # square is less than number (target),
            # mid_index is too small
            # continue to search in right half
            start_index = mid_index + 1
        else:
            # square is greater than number,
            # mid_index is too large
            # continue to search in left half
            end_index = mid_index - 1

    return mid_index


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")


"""
    naive solution, run-time is: O(n)
    need to get to faster run-time of O(log n)
"""


def square_root_naive(number):
    prev = 0

    if number == 0:
        return 0

    for i in range(0, number + 1):
        square = i * i
        if square > number:
            break

        prev = i

        if square == number:
            return i

    return prev


print("Pass" if (3 == square_root_naive(9)) else "Fail")
print("Pass" if (0 == square_root_naive(0)) else "Fail")
print("Pass" if (4 == square_root_naive(16)) else "Fail")
print("Pass" if (1 == square_root_naive(1)) else "Fail")
print("Pass" if (5 == square_root_naive(27)) else "Fail")

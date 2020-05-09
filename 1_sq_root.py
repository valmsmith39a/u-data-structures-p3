def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
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


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# brute force solution, run-time is: O(n)
# need to achieve better time complexity

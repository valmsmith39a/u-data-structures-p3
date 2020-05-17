## Explanation

### Discussion
    At first I tried a naive approach of iterating from 0 to 
    the target number until I found the square root or the next closest square root.
    But the time complexity achieved was only O(n).

    Then I used a binary search approach to find the solution in O(log n) time.
    We can use binary search in this situation because the search set is ordered.

### Time and Space Complexity
    In binary search, every time the number of inputs double (2^x), the number of iterations
    through our while loop increases by 1. The number of cycles is x + 1. 

    To find x, we can use logarithms. For example, 2^3 = 8 and 3 = log (8).
    Similarly, 2^x = n, so x = log (n).

    For number of cycles in binary search, we have 
    
    2^x + 1 = n 

    2^x = n - 1 

    x = log (n - 1 )

    So time complexity is O(log(n-1)) => O(log n)

    Space complexity of binary search is O(1) because as n increases, the space consumed remains constant.

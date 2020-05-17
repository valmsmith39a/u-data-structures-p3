## Explanation

### Discussion
The key concept I used to solve this problem was to insert the largest digit in the largest place value.
I sorted the list from smallest to largest and used the ordered list to fill 2 sub-arrays that formed
the 2 numbers with the greatest sum.

### Time and Space Complexity

I used quicksort to create an ordered list, which runs in O(n log n) time. The loop to fill the 2 sub-arrays
take O(n) time. Overall the running time is O(n log n).

To solve the problem I created 2 sub-arrays which would take O(n) space.

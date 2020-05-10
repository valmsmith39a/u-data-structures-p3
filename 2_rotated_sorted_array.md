## Explanation

### Discussion

If the array was not rotated, then we could simply use the binary search algorithm.

However, the array is rotated, so we must first find the pivot index at which the array is rotated.

Then we can run binary search on the sub-array up to the pivot, and again on the sub-array after the pivot.

### Time Complexity

We run the binary search algorithm 3 times for a run-time of 3 * O(log n) => O(log n)

### Space complexity

We don't create any new data structures other than the given input list, so our program runs in O(1) space. 

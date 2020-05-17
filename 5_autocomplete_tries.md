## Explanation

### Time and Space Complexity

Inserting the valid values into a trie, in the worst case, takes O(m*n) time and space, m = number of words, n = number of characters in each word.

For lookup, the time complexity is O(n), where n = length of the prefix. We don't create new data structures in lookup so the 
space complexity is O(1).
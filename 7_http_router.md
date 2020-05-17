## Explanation

### Time and Space Complexity

Inserting the routes in the trie, in the worse case, takes O(m*n) time and space, where m = number of routes and 
n = number of parts contained in a path (split by "/").

For lookup, the time complexity is O(n), where n = number of parts in a path. We don't create new data structures based on the number of parts in the lookup, so the space complexity is O(1).

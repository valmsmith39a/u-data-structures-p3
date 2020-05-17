# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, some_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for part in path:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]

    def find(self, some_handler):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class RouteTrieNode:
    def __init__(self, some_handler):
        # Initialize the node with children as before, plus a handler
        self.routes = {}
        self.max_depth = 0

    def insert(self, word):
        # Insert the node as before
        self.routes[word] = RouteTrieNode(word)

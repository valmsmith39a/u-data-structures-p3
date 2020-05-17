"""
take a URL path like "/", "/about", or "/ blog/2019-01-15/my-awesome-blog-post

dynamic web server

content from a handler 

Trie will contain parts of the http path at each node, building from the root node

Which function will handle the http request

For this exercise, just need to make sure we go the correct *handler*

Split by the "/"

Path with "/about/me"

(root, None) -> ("about", None) -> ("me", "About Me handler")

don't need suffixes

don't need endOfWord property

"""

# The Router class will wrap the Trie and handle

# A RouteTrie will store our routes and their associated handlers


class RouteTrieNode:
    def __init__(self, handler=""):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, part, handler="default handler"):
        # Insert the node as before
        self.children[part] = RouteTrieNode(handler)


class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for part in path:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]

        # Only assign handler to the leaf (deepest) node of this path
        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.

        current_node = self.root

        for part in path:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node


class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.routes.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_parts = self.split_path(path)
        path_node = self.routes.find(path_parts)
        return path_node.handler if path_node and path_node.handler else "no handler found"

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here

        if path == '/' or path == '':
            return []

        # Ex ['home', 'about']
        # Note that "/" is the root node with handler ex "root handler"
        return path.split("/")[1:]

####################################

# Test route trie node
# route_trie_node = RouteTrieNode('root handler')
# print(route_trie_node)
# print(route_trie_node.children)
# print(route_trie_node.handler)

# Test route trie node insert
# route_trie_node.insert('about', 'about handler')
# print(route_trie_node)
# print(route_trie_node.children)
# print(route_trie_node.children['about'])

# Test Route Trie
# route_trie = RouteTrie('some root handler')
# print(route_trie.root.children)
# print(route_trie.root.handler)
# path = ["home", "about"]
# route_trie.insert(path, "home about handler")
# print(route_trie.root.children)
# {'home': <__main__.RouteTrieNode object at 0x10eed0610>}
# print(route_trie.root.children['home'].children)
# {'about': <__main__.RouteTrieNode object at 0x10eed0650>}
# print(route_trie.find(path).handler)
# home about handler

# Test Router
# test_path = "/home/about"
# test_handler = "home about handler from router"
# router = Router("root handler", "not found handler")
# print(router.routes.root.children)
# {}
# router.add_handler(test_path, test_handler)
# print(router.routes.root.children)
# {'': <__main__.RouteTrieNode object at 0x106881950>}
# print(router.routes.root.children[''].children)
# {'home': <__main__.RouteTrieNode object at 0x109ea2950>}
# print(router.routes.root.children[''].children['home'].children)
# {'about': <__main__.RouteTrieNode object at 0x109ea2990>}
# print(router.lookup(test_path))
# home about handler from router


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route
# print(router.routes.root.children['home'].children['about'].handler)
# about handler

# print(router.routes.root.handler)

# some lookups with the expected output
print(router.lookup(""))
# should print 'root handler'
print(router.lookup("/home"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))
# should print 'about handler'
print(router.lookup("/home/about/"))
# should print 'about handler' or None if you did not handle trailing slashes
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))

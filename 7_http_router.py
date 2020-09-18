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

# Here are some test cases and expected outputs you can use to test your implementation


# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup(""))
# should print 'root handler'
print(router.lookup("/home"))
# should print 'not found handler' or no handler found if you did not implement one
print(router.lookup("/home/about"))
# should print 'about handler'
print(router.lookup("/home/about/"))
# should print 'about handler' or 'no handler found' if you did not handle trailing slashes
print(router.lookup("/home/about/me"))
# should print 'no handler found' or None if you did not implement one

router.add_handler("/home/contact", "contact handler")
router.add_handler("/home/projects", "projects handler")
router.add_handler("/home/projects/ai", "ai handler")
router.add_handler("/home/projects/quantum", "quantum handler")
router.add_handler("/home/projects/genomics", "genomics handler")

print(router.lookup("/home/contact"))
# should print 'contact handler'
print(router.lookup("/home/projects"))
# should print 'projects handler'
print(router.lookup("/home/projects/ai"))
# should print 'ai handler'
print(router.lookup("/home/projects/quantum"))
# should print 'quantum handler'
print(router.lookup("/home/projects/genomics"))
# should print 'genomics handler'

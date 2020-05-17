"""

autocomplete

basic_trie = {
    'a': {
        'd': {
            'd': {
                is_word: True
            },
            'a': {
                is_word: True
            }
            is_word: False
        },
        't': {
            is_word: True
        }
        is_word: True
    }
}

* root node would be the top level object
* 'a' would be part of children of top level object

* type a, shows options for other characters in the child that can form a word
    * want to show at, add, ada
    * want to show first x number of words that could be valid words
    * traverse the trie until reach 'is_word' == True and collect those words

* example, trie contains the words 'bear', 'bearable', 'bearish"
    * prefix 'b', return all the suffixes
        * ['ear', 'earable', 'earish']
"""

# Represents a single node in the Trie


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        suffix_list = []
        if self.is_word:
            suffix_list.append(suffix)

        for char, child in self.children.items():
            new_suffix = suffix + char
            suffix_list.extend(child.suffixes(new_suffix))

        return suffix_list

# The Trie itself containing the root node and insert/find functions


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word


# Test TrieNode
# trie_node = TrieNode()
# print(trie_node)
# print(trie_node.is_word)
# print(trie_node.children)
# trie_node.insert('a')
# print(trie_node.is_word)
# print(trie_node.children)
# print(trie_node.children['a'].children)

# Test Trie
# trie = Trie()
# print(trie)
# print(trie.root.is_word)
# print(trie.root.children)

# trie.insert('bear')
# print(trie.root.children['b'].children)
# print(trie.root.children['b'].children['e'].children)
# print(trie.find('b'))
# print(trie.find('bear'))

# Test suffixes
trie = Trie()
trie.insert('fun')
trie.insert('function')
trie.insert('factory')
# print(trie.find('fun'))
# print(trie.find('function'))
# print(trie.root.children['f'].children)
# {'u': <__main__.TrieNode object at 0x101220690>, 'a': <__main__.TrieNode object at 0x101220850>}

# for f node, expect to return "un", "unction", "actory"
print(trie.root.children['f'].suffixes())

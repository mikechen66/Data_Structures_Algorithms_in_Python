

# trie_build.py


"""
The prefix tree (trie) is the most facinating because of its simplicity, elegance, and practical 
applications. we’ll implement a trie in Python from scratch. We’ll test that our code works using 
Python’s unittest library.  Search engines like Google are able to quickly auto-fill your search 
box with suggestions that start with whatever you’ve typed?  Take this as an example:

How would you go about implementing this behavior, all other complex considerations aside?  The 
verynaive approach is to take the text that the user has typed so far—like a or app—and check if 
any words in our database start with that substring, using a linear search. That would maybe work 
for search engines with a relatively small database.  

But Google deals with billions of queries, so that would hardly be efficient. It gets even more 
inefficient the longer the substring becomes. The efficient answer to the problem is a neat little 
data structure known as a prefix tree. It’s just a tree (not necessarily a binary tree) that 
serves a special purpose.
"""


class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.children = dict()
        self.is_word = False  


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True 
    def find(self, word):
        """
        Returns the TrieNode representing the given word if it exists
        and None otherwise.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        # None returned implicitly if this is False
        if current.is_word:
            return current
    def starts_with(self, prefix):
        """
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        """
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                # Could also just return words since it's empty by default
                return list()
            current = current.children[char]
        self.__child_words_for(current, words)
        return words
    def __child_words_for(self, node, words):
        """
        Cycles through all children of node recursively, adding them to 
        words if they constitute whole words (as opposed to merely prefixes).
        """
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)
    def size(self, current = None):
        """
        Returns the size of this prefix tree, defined as the total number 
        of nodes in the tree.By default, get the size of the whole trie, 
        starting at the root
        """
        if not current:
            current = self.root
        count = 1
        for letter in current.children:
            count += self.size(current.children[letter])
        return count


if __name__ == '__main__':
    trie = PrefixTree()
    trie.insert('apple')
    trie.insert('app')
    trie.insert('aposematic')
    trie.insert('appreciate')
    trie.insert('book')
    trie.insert('bad')
    trie.insert('bear')
    trie.insert('bat')
    print(trie.starts_with('app'))


# Output:

"""
['app', 'apple', 'appreciate']
"""

#########################################################################################################


# assertEqual() function is listed in unittest module


import unittest
from trie import PrefixTree


class TrieTest(unittest.TestCase):
    def setUp(self):
        self.trie = PrefixTree()
    def test_trie_size(self):
        self.trie.insert('apple')
        self.assertEqual(self.trie.size(), 6)
    def test_prefix_not_found_as_whole_word(self):
        self.trie.insert('apple')
        self.trie.insert('appreciate')
        self.assertEqual(self.trie.find('app'), None)
    def test_prefix_is_also_whole_word(self):
        self.trie.insert('apple')
        self.trie.insert('appreciate')
        self.trie.insert('app')
        # 10: [app], [appr], [appre], [apprec], [appreci], [apprecia]
        # [appreciat], [appreciate], [appl], and [apple]
        self.assertEqual(self.trie.size(self.trie.find('app')), 10)
        self.assertEqual(self.trie.find('app').is_word, True)
    def test_starts_with(self):
        self.trie.insert('apple')
        self.trie.insert('appreciate')
        self.trie.insert('aposematic')
        self.trie.insert('apoplectic')
        self.trie.insert('appendix')
        self.assertEqual(self.trie.starts_with('app'), ['apple', 'appreciate', 'appendix'])
    def test_starts_with_self(self):
        self.trie.insert('app')
        self.assertEqual(self.trie.starts_with('app'), ['app'])
    def test_bigger_size(self):
        self.trie.insert('bad')
        self.trie.insert('bat')
        self.trie.insert('cat')
        self.trie.insert('cage')
        self.assertEqual(self.trie.size(), 10)
    def test_starts_with_empty_and_no_words(self):
        self.assertEqual(self.trie.starts_with(''), [])
    def test_starts_with_empty_returns_all_words(self):
        self.trie.insert('bad')
        self.trie.insert('bat')
        self.trie.insert('cat')
        self.trie.insert('cage')
        self.assertEqual(self.trie.starts_with(''), ['bad', 'bat', 'cat', 'cage'])


if __name__ == '__main__':
    unittest.main()


# Output:

"""
Ran 8 tests in 0.001s

OK
"""
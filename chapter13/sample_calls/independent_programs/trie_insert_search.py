

# trie_insert_search.py


"""
A trie (derived from retrieval) is a multi-way tree data structure used for storing 
strings over an alphabet. It is used to store a large amount of strings. The pattern 
matching can be done efficiently using tries.

The trie shows words like allot, alone, ant, and, are, bat, bad. The idea is that all 
strings sharing common prefix should come from a common node. The tries are used in 
spell checking programs.

Preprocessing pattern improves the performance of pattern matching algorithm. But if 
a text is very large then it is better to preprocess text instead of pattern for 
efficient search.

A trie is a data structure that supports pattern matching queries in time proportional 
to the pattern size.

If we store keys in a binary search tree, a well balanced BST will need time proportional 
to M * log N, where M is the maximum string length and N is the number of keys in the tree. 
Using Trie, the key can be searched in O(M) time. However, the penalty is on Trie storage 
requirements (Please refer to Applications of Trie for more details).

"""


class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [None]*26
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
    def _charToIndex(self,ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch)-ord('a')
    def insert(self,key):
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        # mark last node as leaf
        pCrawl.isEndOfWord = True
    def search(self, key):
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
            "Present in trie"]
    # Trie object
    t = Trie()
    # Construct trie
    for key in keys:
        t.insert(key)
    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))


if __name__ == '__main__':
    main()


# Output:

"""
the ---- Present in trie
these ---- Not present in trie
their ---- Present in trie
thaw ---- Not present in trie
"""
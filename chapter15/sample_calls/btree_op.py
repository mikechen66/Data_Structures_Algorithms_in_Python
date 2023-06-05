

# btree_case.py


"""
In practical applications, the order m of B trees is very large (usually greater than 100), 
so even if a large amount of data is stored, the height of B trees is still relatively small. 
Each node stores the key and the data corresponding to the key, as well as the pointer to 
the child's node. 

We call a key and its corresponding data a record. In the database, we use B tree (and B+ 
tree) as the index structure to speed up the query. At this time, key in B tree represents 
the key, and data represents the logical address of the entry corresponding to this key on 
the hard disk.

In order to make the code easier to write, we can define the length of the array storing 
records in the node as m instead of m-1, so that when the node at the bottom is inserted 
as a record to the upper layer due to splitting, the upper layer has extra space to store 
the record. At the same time, each node can also store a reference to its parent, so there 
is no necessary to write a recursive snippet. 


1. Insertion 

The insertion operation refers to inserting a key value pair of (key, value) into a record. 
If a key-value pair that needs to be inserted already exists in the B-tree, replace the old 
value with the value that needs to be inserted. If the key does not exist in the B-tree, it 
must be an insertion operation in the leaf node.


1) Find the leaf node and insert it according to the value of the key to be inserted.

2) Judge wehter the number of keys in the current node is less than or equal to m-1. If it is,
  it ends. Otherwise, the following third step is carried out.

3) Split the key in the middle of the node into left and right parts, and then insert the 
   middle key into the parent node. The left subtree of the key points to the left half of 
   the split, and the right subtree to the right half. Then, point the current node to the 
   parent node and continue with step 3.


2. Deletion

Deleting a record means removing a record according to a given key. If there is no record 
corresponding to in the B-Tree, the record fails to be deleted.

1) If the current key to be deleted is located on a non-leaf node, overwrite the key to be 
   deleted with the successor key (or the successive record), and then delete the successive 
   key in the sub-branch where the successor key is located. In this case, the successing key 
   must be located on the leaf node, and the process is similar to deleting nodes in binary 
   search tree to delete nodes. Perform Step 2 after deleting this record

2) If the number of keys on the node is greater than or equal to Math.ceil(m/2)-1, the deletion 
   operation is over. Otherwise, go to Step 3 as follows. 

3) If the number of keys of sibling node is greater than Math.ceil(m/2)-1, the deletion operation 
   is over after the keys in the parent node moves down to the node and one of keys in the sibling 
   node moves up. Otherwise, we move the key in the parent node down and merge it with the keys 
   in both the current node and its sibling node to form a new node. The two pointers of children
   corresponding to the parent becomes one child pointer to the new node. Then the pointer of the 
   current node points to the parent, and repeat step 2.
"""


from random import shuffle
import random


root_node = None


M = 9


class Logger(object):
    @classmethod
    def tree(cls, node, child_name, dsc, depth):
        if depth == 0:
            head = "|   " * depth
            print(head + "+--" + dsc(node))
            depth = depth + 1
        for child in getattr(node, child_name):
            head = "|   " * depth
            print(head + "+--" + dsc(child))
            cls.tree(child, child_name, dsc, depth + 1)


class BKeyword(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data


class BTree(object):
    def __init__(self):
        self._parent: BTree = None
        self.keywords = []
        self.child_nodes = []
    # Set the parent
    def set_parent(self, node):
        self._parent = node
        if node.get_parent() is None:
            global root_node
            root_node = node.get_parent()
    # Obtain the parent node 
    def get_parent(self):
        return self._parent
    # Add the child node into the designated position
    def insert_child_node(self, index, add_node):
        add_node.set_parent(self)
        self.child_nodes.insert(index, add_node)
    # Add the child node 
    def append_child_node(self, add_node):
        add_node.set_parent(self)
        self.child_nodes.append(add_node)
    # Find out a suitable insertion position
    def find_add_index(self, add_word):
        if len(self.keywords) == 0:
            return 0
        index = 0
        while True:
            if index >= len(self.keywords):
                break
            key = self.keywords[index].key
            if add_word.key < key:
                break
            index = index + 1
        return index
    # Insert the data into a suitbale position
    def blind_mate(self, word: BKeyword) -> int:
        index = self.find_add_index(word)
        self.keywords.insert(index, word)
    def split(self):
        # Split the node
        parent, center_keyword, left_node, right_node = self.split_to_child()
        # Add two new nodes into the parent
        parent_add_index = parent.find_add_index(center_keyword)
        parent.insert_child_node(parent_add_index, right_node)
        parent.insert_child_node(parent_add_index, left_node)
        # Remove self that include m keywords 
        if self in parent.child_nodes:
            parent.child_nodes.remove(self)
        parent.add_word(center_keyword, force=True)
        # Assign self to root(redefine the root node)
        root = self
        while root.get_parent() is not None:
            root = root.get_parent()
        global root_node
        root_node = root
    def split_to_child(self):
        center_keyword = self.keywords[int((M-1)/2)]
        if self.get_parent() is None:
            self.set_parent(BTree())
        left_node = BTree()
        right_node = BTree()
        for keyword in self.keywords:
            if keyword.key < center_keyword.key:
                left_node.keywords.append(keyword)
            elif keyword.key > center_keyword.key:
                right_node.keywords.append(keyword)
        for i in range(len(self.child_nodes)):
            if i <= int((len(self.child_nodes) - 1)/2):
                left_node.append_child_node(self.child_nodes[i])
            else:
                right_node.append_child_node(self.child_nodes[i])
        return self.get_parent(), center_keyword, left_node, right_node
    # Newly add keyword with force carrying bit
    def add_word(self, keyword, force=False):
        if keyword.key == 0:
            print("")
        # Leaf node or add with carrying bit 
        if len(self.child_nodes) == 0 or force:
            if keyword.key == 20:
                print("")
            self.blind_mate(keyword)
            if len(self.keywords) == M:
                # Start to split
                print("Added keyword:" + str(keyword.key) + ", reach M and then split")
                self.split()
        else: # As keyword > 100
            # Non-leaf node
            index = self.find_add_index(keyword)
            if index >= len(self.child_nodes):
                index = index - 1
            self.child_nodes[index].add_word(keyword)


def show_tree(node):
    print("\n**********************************************")
    def dsc(node):
        s = ''
        for keyword in node.keywords:
            s = s + str(keyword.key) + ','
        s = s[:-1]
        return s
    Logger.tree(node, 'child_nodes', dsc,  0)
    print("**********************************************")


def prepare():
    array = []
    number = 0
    for i in range(200):
        number = number + random.randint(1, 4)
        array.append(number)
    shuffle(array)
    return array


if __name__ == '__main__':
    root_node = BTree()
    array = prepare()
    for i in array:
        keyword = BKeyword(i, "data" + str(i))
        root_node.add_word(keyword)
    show_tree(root_node)



# Output:

"""
Added keyword:277, reach M and then split
Added keyword:337, reach M and then split
Added keyword:75, reach M and then split
Added keyword:74, reach M and then split
Added keyword:323, reach M and then split
Added keyword:248, reach M and then split
Added keyword:477, reach M and then split
Added keyword:114, reach M and then split
Added keyword:296, reach M and then split
Added keyword:337, reach M and then split
Added keyword:33, reach M and then split
Added keyword:211, reach M and then split
Added keyword:150, reach M and then split
Added keyword:468, reach M and then split
Added keyword:16, reach M and then split
Added keyword:91, reach M and then split
Added keyword:93, reach M and then split
Added keyword:36, reach M and then split
Added keyword:436, reach M and then split
Added keyword:347, reach M and then split
Added keyword:316, reach M and then split
Added keyword:418, reach M and then split
Added keyword:410, reach M and then split
Added keyword:199, reach M and then split
Added keyword:214, reach M and then split
Added keyword:506, reach M and then split
Added keyword:461, reach M and then split
Added keyword:99, reach M and then split
Added keyword:256, reach M and then split
Added keyword:171, reach M and then split
Added keyword:385, reach M and then split
Added keyword:135, reach M and then split
Added keyword:134, reach M and then split

**********************************************
+--117,186,271,388
|   +--16,33,58,75,93,105
|   |   +--1,2,3,6,8,12
|   |   +--17,21,22,24,28,31,32
|   |   +--36,40,43,45,48,50,52,56
|   |   +--62,63,67,68,71,74
|   |   +--78,79,80,83,87,90,91
|   |   +--97,98,99,103
|   |   +--107,111,113,114,116
|   +--134,150,163,175
|   |   +--121,123,126,130
|   |   +--135,138,142,146
|   |   +--151,153,155,159
|   |   +--165,167,169,171
|   |   +--178,179,183,185
|   +--211,227,241,252
|   |   +--188,191,195,197,199,203,205,209
|   |   +--214,218,221,223,226
|   |   +--229,232,233,234,237,239
|   |   +--243,244,248,251
|   |   +--256,260,263,265,268,269
|   +--288,316,337,363,374
|   |   +--273,276,277,278,282,284,286
|   |   +--292,296,299,303,306,310,313
|   |   +--319,323,326,327,331,333,336
|   |   +--340,343,347,350,354,357,358,359
|   |   +--366,369,370,373
|   |   +--376,379,383,385
|   +--410,429,442,458,477,494
|   |   +--390,394,397,398,402,403,407
|   |   +--411,414,418,422,423,424,428
|   |   +--431,433,436,437,440,441
|   |   +--445,447,451,455,456
|   |   +--461,465,468,471,473
|   |   +--479,482,485,486,487,488,490
|   |   +--497,501,505,506,508
**********************************************
"""
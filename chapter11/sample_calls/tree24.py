

# tree24.py
# demonstrate 2-4 tree(also called 2-3-4 tree)

"""
(2,4) tree is also called (a,b) tree that is multiway search tree such that each node has between a and
b children and stores between a−1 and b−1 entries. The algorithms for searching, inserting, and removing 
entries in an (a, b) tree are straightforward generalizations of the corresponding ones for (2, 4) trees.

An (a,b) tree, where parameters a and b are integers such that 2 ≤ a ≤ (b + 1)/2, is a multiway search 
tree T with the following additional restrictions:

Size Property: Each internal node has at least a children, unless it is the root, and
has at most b children.

Depth Property: All the external nodes have the same depth.
"""


class DataItem:
    # With instances customized to a specific initial state
    def __init__(self, dd): 
        self.ddata = dd                              # one piece of data
    def display_item(self):                          # format " /27"
        print('/', self.ddata)


class Node:
    #  Use a convention: name prefixed with an underscore, to treat them as non-public part
    _ORDER = 4
    def __init__(self):
        self._num_items = 0
        self._pparent = None
        self._child_array = []                       # array of nodes
        self._item_array = []                        # array of data
        for j in range(self._ORDER):                 # initialize arrays
            self._child_array.append(None)
        for k in range(self._ORDER - 1):
            self._item_array.append(None)
    # Connect child to this node
    def connect_child(self, childnum, pchild):
        self._child_array[childnum] = pchild
        if pchild:
            pchild._pparent = self
    # Disconnect child from this node, return it
    def disconnect_child(self, childnum):
        temnode = self._child_array[childnum]
        self._child_array[childnum] = None
        return temnode
    def get_child(self, childnum):
        return self._child_array[childnum]
    def get_parent(self):
        return self._pparent
    def is_leaf(self):
        return not self._child_array[0]
    def get_num_items(self):
        return self._num_items
    def get_item(self, index):                       # get DataItem at index
        return self._item_array[index]
    def is_full(self):
        return self._num_items == self._ORDER - 1
    def find_item(self, key):                        # return index of
        for j in range(self._ORDER-1):               # item (within node)
            if not self._item_array[j]:              # if found
                break                                # otherwise,
            elif self._item_array[j].ddata == key:   # return -1
                return j
        return -1
    def insert_item(self, newitem):
        # Assume the node is not full
        self._num_items += 1                         # will add new item
        newkey = newitem.ddata                       # key of new item
        for j in reversed(range(self._ORDER-1)):     # start on righ
            if self._item_array[j] == None:          # if item null,
                pass                                 # go left one cell
            else:                                    # not null,
                itskey = self._item_array[j].ddata   # get its key
                if newkey < itskey:                  # if it's bigger
                    self._item_array[j+1] = self._item_array[j]  # shift it right
                else:
                    self._item_array[j+1] = newitem  # insert new item
                    return j + 1                     # return index to new item
        self._item_array[0] = newitem                # insert new item
        return 0
    def remove_item(self):                           # remove largest item
        # assume node not empty
        temp = self._item_array[self._num_items-1]   # save item
        self._item_array[self._num_items-1] = None   # disconnect it
        self._num_items -= 1                         # one less item
        return temp                                  # return item
    def display_node(self):                          # format "/24/56/74"
        for j in range(self._num_items):
            self._item_array[j].display_item()       # format "/56"
        print('/')                                   # final "/"


class Tree24:
    # Use a convention: name prefixed with an underscore, to treat them as non-public part
    def __init__(self):
        self._proot = Node()                         # root node(see the above Node class)
    def find(self, key):
        curnode = self._proot                        # start at root (see the above Node class)
        while True:
            childnumber = curnode.find_item(key)
            if childnumber != -1:
                return childnumber                   # found it
            elif curnode.is_leaf():
                return -1                            # can't find it
            else:                                    # search deeper
                curnode = self.get_next_child(curnode, key)
    def insert(self, dvalue):                        # insert a DataItem
        curnode = self._proot                        # See the Node class
        tempitem = DataItem(dvalue)                  # See the above DataItem class
        while True:
            if curnode.is_full():                    # if node full,
                self.split(curnode)                  # split it
                curnode = curnode.get_parent()       # back up
                # search once
                curnode = self.get_next_child(curnode, dvalue)
            elif curnode.is_leaf():                  # if node is leaf,
                break                                # go insert
            # node is not full, not a leaf; so go to lower level
            else:
                curnode = self.get_next_child(curnode, dvalue)
        curnode.insert_item(tempitem)                # insert new temporary item
    def split(self, node):                           # split the node
        # Assume the node is full
        itemc = node.remove_item()                   # remove items from
        itemb = node.remove_item()                   # this node
        child2 = node.disconnect_child(2)            # remove children
        child3 = node.disconnect_child(3)            # from this node
        newright = Node()                            # make new node
        if node == self._proot:                      # if this is the root(Node)
            self._proot = Node()                     # make new root
            pparent = self._proot                    # root is our parent
            self._proot.connect_child(0, node)       # connect to parent
        else:                                        # this node not the root
            pparent = node.get_parent()              # get parent
        # deal with parent
        index = pparent.insert_item(itemb)           # item B to parent
        n = pparent.get_num_items()                  # total items?
        j = n - 1                                    # move parent's
        while j > index:                             # connections
            ptemp = pparent.disconnect_child(j)      # one child
            pparent.connect_child(j+1, ptemp)        # to the right
            j -= 1
        pparent.connect_child(index+1, newright)     # connect the newright to parent
        # Deal with newright
        newright.insert_item(itemc)                  # item C to the newright
        newright.connect_child(0, child2)            # connect to 0 and 1
        newright.connect_child(1, child3)            # on the newright
    # Get appropriate child of node during search of value
    def get_next_child(self, pnode, value):          # Call the function with passing Node() and key
        # Assume node is not empty, not full, not a leaf
        numitems = pnode.get_num_items()
        for j in range(numitems):                    # for each item in node
            if value < pnode.get_item(j).ddata:      # are we less?
                return pnode.get_child(j)            # return left child
        else:  
            return pnode.get_child(j + 1)            # return right child
    def display_tree(self):
        self.rec_display_tree(self._proot, 0, 0)
    def rec_display_tree(self, node, level, childnumber):
        print('level=', level, 'child=', childnumber)
        node.display_node()                          # display the node
        # Call ourselves for each child of this node
        numitems = node.get_num_items()
        for j in range(numitems+1):
            nextnode = node.get_child(j)
            if nextnode:
                self.rec_display_tree(nextnode, level+1, j)
            else:
                return


if __name__ == '__main__':
    ptree = Tree24()
    ptree.insert(50)
    ptree.insert(40)
    ptree.insert(60)
    ptree.insert(30)
    ptree.insert(70)
    ptree.display_tree()


# Output:

"""
# Output:

Enter first letter of show, insert, or find: s
level= 0 child= 0
/ 50
/
level= 1 child= 0
/ 30
/ 40
/
level= 1 child= 1
/ 60
/ 70
/
"""

#############################################################################################################


# The following code snippet is interactively shown 

# As Python doesn't support switch, simulating the same with dictionary and functions
def show():
    ptree.display_tree()


def insert():
    # Enter value such as 20, 10, 
    value = int(input('Enter value to insert: '))
    ptree.insert(value)


def find():
    # Enter value such as 40
    value = int(input('Enter value to find: '))
    found = ptree.find(value)
    if found != -1:
        print('Found', value)
    else:
        print('Could not find', value)


case = { 's' : show,
         'i' : insert,
         'f' : find
       }


# It is interactive in the terminal because it has input() functions 

while True:
    print()
    # Enter the first such as s,f,i,s,i,s
    choice = input('Enter first letter of show, insert, or find: ')
    if case.get(choice, None):
        case[choice]()
    else:
        print('Invalid entry')


del ptree



# Output: 

"""
Enter first letter of show, insert, or find: f
Enter value to find: 40
Found 40

Enter first letter of show, insert, or find: i
Enter value to insert: 20

Enter first letter of show, insert, or find: s
level= 0 child= 0
/ 50
/
level= 1 child= 0
/ 20
/ 30
/ 40
/
level= 1 child= 1
/ 60
/ 70
/

Enter first letter of show, insert, or find: i
Enter value to insert: 10

Enter first letter of show, insert, or find: s
level= 0 child= 0
/ 30
/ 50
/
level= 1 child= 0
/ 10
/ 20
/
level= 1 child= 1
/ 40
/
level= 1 child= 2
/ 60
/ 70
/
"""
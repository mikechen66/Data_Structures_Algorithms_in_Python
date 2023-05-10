

# 2_4_tree.py
# demonstrate 2-4 tree(also called 2-3-4 tree)


class DataItem:
    # With instances customized to a specific initial state
    def __init__(self, dd): 
        self.dData = dd                              # one piece of data
    def displayItem(self):                           # format " /27"
        print('/', self.dData)


class Node:
    #  Use a convention: name prefixed with an underscore, to treat them as non-public part
    _ORDER = 4
    def __init__(self):
        self._numItems = 0
        self._pParent = None
        self._childArray = []                        # array of nodes
        self._itemArray = []                         # array of data
        for j in range(self._ORDER):                 # initialize arrays
            self._childArray.append(None)
        for k in range(self._ORDER - 1):
            self._itemArray.append(None)
    # Connect child to this node
    def connectChild(self, childNum, pChild):
        self._childArray[childNum] = pChild
        if pChild:
            pChild._pParent = self
    # Disconnect child from this node, return it
    def disconnectChild(self, childNum):
        pTempNode = self._childArray[childNum]
        self._childArray[childNum] = None
        return pTempNode
    def getChild(self, childNum):
        return self._childArray[childNum]
    def getParent(self):
        return self._pParent
    def isLeaf(self):
        return not self._childArray[0]
    def getNumItems(self):
        return self._numItems
    def getItem(self, index):                        # get DataItem at index
        return self._itemArray[index]
    def isFull(self):
        return self._numItems==self._ORDER - 1
    def findItem(self, key):                         # return index of
        for j in range(self._ORDER-1):               # item (within node)
            if not self._itemArray[j]:               # if found
                break                                # otherwise,
            elif self._itemArray[j].dData == key:    # return -1
                return j
        return -1
    def insertItem(self, pNewItem):
        # Assume the node is not full
        self._numItems += 1                          # will add new item
        newKey = pNewItem.dData #key of new item
        for j in reversed(range(self._ORDER-1)):     # start on righ
            if self._itemArray[j] == None:           # if item null,
                pass                                 # go left one cell
            else:                                    # not null,
                itsKey = self._itemArray[j].dData    # get its key
                if newKey < itsKey:                  # if it's bigger
                    self._itemArray[j+1] = self._itemArray[j]  # shift it right
                else:
                    self._itemArray[j+1] = pNewItem  #insert new item
                    return j+1                       # return index to new item
        self._itemArray[0] = pNewItem                # insert new item
        return 0
    def removeItem(self):   #remove largest item
        #assumes node not empty
        pTemp = self._itemArray[self._numItems-1]    # save item
        self._itemArray[self._numItems-1] = None     # disconnect it
        self._numItems -= 1#one less item
        return pTemp#return item
    def displayNode(self):  #format "/24/56/74"
        for j in range(self._numItems):
            self._itemArray[j].displayItem()         # format "/56"
        print('/')  #final "/"


class Tree24:
    # Use a convention: name prefixed with an underscore, to treat them as non-public part
    def __init__(self):
        self._pRoot = Node()                         # root node
    def find(self, key):
        pCurNode = self._pRoot                       # start at root
        while True:
            childNumber=pCurNode.findItem(key)
            if childNumber != -1:
                return childNumber                   # found it
            elif pCurNode.isLeaf():
                return -1                            # can't find it
            else:   #search deeper
                pCurNode = self.getNextChild(pCurNode, key)
    def insert(self, dValue):                        # insert a DataItem
        pCurNode = self._pRoot
        pTempItem = DataItem(dValue)
        while True:
            if pCurNode.isFull():                    # if node full,
                self.split(pCurNode)                 # split it
                pCurNode = pCurNode.getParent()      # back up
                # search once
                pCurNode = self.getNextChild(pCurNode, dValue)
            elif pCurNode.isLeaf():                  # if node is leaf,
                break                                # go insert
            # node is not full, not a leaf; so go to lower level
            else:
                pCurNode = self.getNextChild(pCurNode, dValue)
        pCurNode.insertItem(pTempItem)               # insert new item
    def split(self, pThisNode):                      # split the node
        # assumes node is full
        pItemC = pThisNode.removeItem()              # remove items from
        pItemB = pThisNode.removeItem()              # this node
        pChild2 = pThisNode.disconnectChild(2)       # remove children
        pChild3 = pThisNode.disconnectChild(3)       # from this node
        pNewRight = Node()                           # make new node
        if pThisNode == self._pRoot:                 # if this is the root,
            self._pRoot = Node()                     # make new root
            pParent = self._pRoot                    # root is our parent
            self._pRoot.connectChild(0, pThisNode)   # connect to parent
        else:                                        # this node not the root
            pParent = pThisNode.getParent()          # get parent
        # deal with parent
        itemIndex = pParent.insertItem(pItemB)       # item B to parent
        n = pParent.getNumItems()                    # total items?
        j = n-1                                      # move parent's
        while j > itemIndex:                         # connections
            pTemp = pParent.disconnectChild(j)       # one child
            pParent.connectChild(j+1, pTemp)         # to the right
            j -= 1
                                                     # connect newRight to parent
        pParent.connectChild(itemIndex+1, pNewRight)
        # Deal with newRight
        pNewRight.insertItem(pItemC)                 # item C to newRight
        pNewRight.connectChild(0, pChild2)           # connect to 0 and 1
        pNewRight.connectChild(1, pChild3)           # on newRight
    # Get appropriate child of node during search of value
    def getNextChild(self, pNode, theValue):
        # Assume node is not empty, not full, not a leaf
        numItems = pNode.getNumItems()
        for j in range(numItems):                    # for each item in node
            if theValue < pNode.getItem(j).dData:    # are we less?
                return pNode.getChild(j)             # return left child
        else:  
            return pNode.getChild(j + 1)             # return right child
    def displayTree(self):
        self.recDisplayTree(self._pRoot, 0, 0)
    def recDisplayTree(self, pThisNode, level, childNumber):
        print('level=', level, 'child=', childNumber)
        pThisNode.displayNode()                     # display this node
        # Call ourselves for each child of this node
        numItems = pThisNode.getNumItems()
        for j in range(numItems+1):
            pNextNode = pThisNode.getChild(j)
            if pNextNode:
                self.recDisplayTree(pNextNode, level+1, j)
            else:
                return


if __name__ == '__main__':
    pTree = Tree24()
    pTree.insert(50)
    pTree.insert(40)
    pTree.insert(60)
    pTree.insert(30)
    pTree.insert(70)
    pTree.displayTree()



# As Python doesn't support switch, simulating the same with dictionary and functions
def show():
    pTree.displayTree()


def insert():
    # Enter value such as 20, 10, 
    value = int(input('Enter value to insert: '))
    pTree.insert(value)


def find():
    # Enter value such as 40
    value = int(input('Enter value to find: '))
    found = pTree.find(value)
    if found != -1:
        print('Found', value)
    else:
        print('Could not find', value)


case = { 's' : show,
         'i' : insert,
         'f' : find}


while True:
    print()
    # Enter the first such as s,f,i,s,i,s
    choice = input('Enter first letter of show, insert, or find: ')
    if case.get(choice, None):
        case[choice]()
    else:
        print('Invalid entry')


del pTree


# Output:


"""
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
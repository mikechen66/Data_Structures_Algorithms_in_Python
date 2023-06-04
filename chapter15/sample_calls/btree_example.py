

# breee_example.py


import sys


class Node:
    def __init__(self, n=0, isleaf=True):
        self.n = n
        self.keys = []
        self.child = []
        self.leaf = isleaf
    def allocate_node(self, key_max):
        child_max = key_max + 1
        for i in range(key_max):
            self.keys.append(None)
        for i in range(child_max):
            self.child.append(None)
        return self


class BTree:
    def __init__(self, t, root=None):
        self.t = t
        self.max_key = 2*self.t - 1
        self.max_child = self.max_key + 1
        self.root = root
    def split_child(self, x, i):
        z = self._new_node()
        y = x.child[i]
        z.leaf = y.leaf
        z.n = self.t - 1  
        for j in range(self.t-1):
            z.keys[j] = y.keys[j+self.t]    
        if not y.leaf:
            for j in range(self.t):
                z.child[j] = y.child[j+self.t]
        y.n = self.t - 1
        for j in range(x.n+1, i, -1):
            x.child[j] = x.child[j-1]
        x.child[i+1] = z
        for j in range(x.n, i-1, -1):
            x.keys[j] = x.keys[j-1]
        x.keys[i] = y.keys[self.t-1]
        x.n = x.n + 1 
    def insert_nonfull(self, x, k):
        i = x.n
        if x.leaf:
            while i >= 1 and k < x.keys[i-1]:
                x.keys[i] = x.keys[i-1]
                i -= 1
            x.keys[i] = k
            x.n += 1
        else:
            while i >= 1 and k < x.keys[i-1]:
                i -= 1
            i += 1
            if x.child[i-1].n == 2*self.t - 1:
                self.split_child(x, i-1)
                if k > x.keys[i-1]:
                    i += 1
            self.insert_nonfull(x.child[i-1],k)
    def _new_node(self):
        return Node().allocate_node(self.max_key)   
    def insert(self, k):
        if self.root is None:
            node = self._new_node()
            self.root = node    
        r = self.root
        if r.n == 2*self.t - 1:
            s = self._new_node()
            self.root = s
            s.leaf = False
            s.n = 0
            s.child[0] = r
            self.split_child(s, 0)
            self.insert_nonfull(s, k)
        else:
            self.insert_nonfull(r, k)
    def walk(self):
        current = [self.root]
        while current:
            next_current = []
            output = ""
            for node in current:
                if node != None and node.child:
                    next_current.extend(node.child)
                if node != None:
                    output += ''.join(node.keys[0:node.n]) + " "
            print(output)
            current = next_current
    def order(self, tree):
        if tree is not None:
            for i in range(tree.n):
                self.order(tree.child[i])
                print(tree.keys[i], end=" ")
                self.order(tree.child[i+1])
    def search(self, x, k):
        i = 0
        while i <= x.n and k > x.keys[i]:
            i += 1
        if i < x.n and k == x.keys[i]:
            return (x,i)
        elif x.leaf:
            return None
        else:
            return self.search(x.child[i], k)


if __name__=='__main__':
    tree = BTree(3)
    for x in ['G','M','P','X','A','C','D','E','J','K','N','O',
              'R','S','T','U','V','Y','Z','B','Q','L','F']:
        tree.insert(x)
    tree.walk()
    tree.order(tree.root)
    print('\n')
    result = tree.search(tree.root, '1')
    if result != None:
        print("find key :"+result[0].keys[result[1]])
    else:
        print("Do not find key")



# Output:

"""
DJMPT 
ABC EFG KL NO QRS UVXYZ 

A B C D E F G E F G J K L K L M N O N O P Q R S Q R S T U V X Y Z 

Do not find key
"""
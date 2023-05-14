
# skip_list.py


import random


class SkipNode:
    """Represent the node class of skip list"""
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)
    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'


class SkipList:
    """SkipList is the concrete class realization of skip list"""
    def __init__(self, max_level, portion):
        """
        :param max_level: the max level of skiplist
        :param portion: the percentage of i-1 nodes
        """
        self.max_level = max_level
        self.portion = portion
        self.header = self._make_node(self.max_level, None, None)
        self.level = 0            # Current reference level number
        self.n = 0
    def __len__(self):
        # resturn the number of nodes
        return self.n
    def _make_node(self, node_level, key, value):
        """
        Create a new node of the skip list
        :param level: the highest levels of a new node
        :key: key of the new node
        :param value: value of the new node
        :return: return the node(reference)
        """
        node = SkipNode(key, value, node_level)
        return node
    def _random_node_level(self):    # Set up the condition of random number 
        node_level = 0
        while random.random() < self.portion and node_level < self.max_level:
            node_level += 1
        return node_level
    def _utility_search(self, key2search):
        """
        :param key2search: the key of searching node
        :return: (current, cursor): tuple
        """
        cursor = [None] * (self.max_level + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            # While skiplist is empty，current.forward[0] is None
            while current.forward[i] and current.forward[i].key < key2search:
                current = current.forward[i]
            cursor[i] = current
        current = current.forward[0]
        return current, cursor
    def skip_search(self, key2search):
        # While find out the key-value pair of key2search，otherwise KeyError异常
        current, _ = self._utility_search(key2search)
        if current and current.key == key2search:
            return current
        else:
            raise KeyError('key {} does not exist!'.format(key2search))
    def skip_insert(self, key2search, value2insert):
        # The node is obtained after inserting a key-value pari
        current, cursor = self._utility_search(key2search)
        if current and current.key == key2search:
            current.value = value2insert
        else:
            node_level = self._random_node_level()
            if node_level > self.level:
                for i in range(self.level + 1, node_level + 1):
                    cursor[i] = self.header
                self.level = node_level
            node = self._make_node(node_level, key2search, value2insert)
            for i in range(node_level + 1):
                node.forward[i] = cursor[i].forward[i]
                cursor[i].forward[i] = node
            self.n += 1
    def skip_delete(self, key2search):
        # Delete the node which key is key2search
        current, cursor = self._utility_search(key2search)
        if current is not None and current.key == key2search:
            result = current
            for i in range(self.level + 1):
                if cursor[i].forward[i] != current:
                    break
                cursor[i].forward[i] = current.forward[i]
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
            self.n -= 1
            return result
    def skip_display(self):
        print("\n------------Skip List------------")
        header = self.header
        for node_level in range(self.level + 1):
            print("Level {}: ".format(node_level), end=" ")
            node = header.forward[node_level]
            while node is not None:
                print(node.key, end=" ")
                node = node.forward[node_level]
            print('')


if __name__ == '__main__':
    slist = SkipList(10, 0.5)
    slist.skip_insert(3, 5)
    slist.skip_insert(12, 9)
    slist.skip_insert(26, 7)
    slist.skip_insert(7, 13)
    slist.skip_insert(21, 3)
    slist.skip_insert(25, 4)
    slist.skip_insert(6, 6)
    slist.skip_insert(17, 8)
    slist.skip_insert(19, 10)
    slist.skip_insert(9, 14)
    print(len(slist))             # 10
    print(slist.skip_search(3))   # (3, 5)
    print(slist.skip_delete(19))  # (19, 10)
    print(len(slist))             # 9
    slist.skip_display()


# Output:

"""
10
(3, 5)
(19, 10)
9

------------Skip List------------
Level 0:  3 6 7 9 12 17 21 25 26 
Level 1:  6 17 21 25 
Level 2:  6 21 25 
Level 3:  6 21 25 
Level 4:  21 25 
Level 5:  21 
"""
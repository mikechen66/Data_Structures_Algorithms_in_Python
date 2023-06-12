
# avl_tree_traversal.py


"""

1. Environment:

It is necessary to run the script on Python 3.9 or above. If reader has no lower Python Interpreter, 
please log on the following online compiler. 

Python Online Compiler 
https://www.programiz.com/python-programming/online-compiler/


2. dataclasses module:

This module provides a decorator and functions for automatically adding generated special methods 
such as __init__() and __repr__() to user-defined classes. It was originally described in PEP 557.
# from dataclasses import dataclass

https://docs.python.org/3/library/dataclasses.html

3. For reference 

The script is taken from the resource as follows. 

https://www.formosa1544.com/2021/06/06/build-the-forest-in-python-series-avl-tree/
https://github.com/burpeesDaily/forest-python

"""

##########################################################################################################


# 1. metrics.py

"""
Metrics model is dedicated to measure tree performance.
"""


import numpy as np
from typing import Union


class Counter:
    """An incrementing and decrementing counter metric."""
    def __init__(self) -> None:
        self._count = 0
    def increase(self, n: int = 1) -> None:
        """
        Increment the counter.
        Parameters: 
        n: `int`
            The count to be increased.
        """
        self._count += n
    def decrease(self, n: int=1) -> None:
        """
        Decrement the counter.
        Parameters
        n: `int`
            The count to be decreased.
        """
        self._count -= n
    @property
    def count(self) -> int:
        # Return the current count.
        return self._count


class Histogram:
    """A metric which calculates the distribution of a value."""
    def __init__(self) -> None:
        self._values: list[int] = list()
    def update(self, value: int) -> None:
        """
        Add a recorded value.
        Parameters
        value: `int`
            value to be updated
        """
        self._values.append(value)
    def report(self) -> dict:
        # Return the histogram report.
        array = np.array(self._values)
        return {
            "min": array.min(),
            "max": array.max(),
            "medium": np.median(array),
            "mean": array.mean(),
            "stdDev": array.std(),
            "percentile": {
                "75": np.percentile(array, 75),
                "95": np.percentile(array, 95),
                "99": np.percentile(array, 99),
            },
        }


MetricType = Union[Counter, Histogram]


class MetricRegistry:
    """A registry for metric instances."""
    def __init__(self) -> None:
        self._registry: dict[str, MetricType] = dict()
    def register(self, name: str, metric: MetricType) -> None:
        """
        Given a metric, register it under the given name.
        Parameters
        name: `str`
            The name of the metric
        metric: `MetricType`
            The type of the metric
        """
        self._registry[name] = metric
    def get_metric(self, name: str) -> MetricType:
        """
        Return the metric by the given name.
        Parameters
        name: `str`
            The name of the metric
        Returns
            `MetricType`
            The metric instance by the given name.
        """
        return self._registry[name]


##########################################################################################################


# 2. tree_exceptions.py


# Tree Exception Definitions.


class DuplicateKeyError(Exception):
    """Raised when a key already exists."""
    def __init__(self, key: str) -> None:
        Exception.__init__(self, f"{key} already exists.")


##########################################################################################################


# 3. avl_tree.py


from dataclasses import dataclass
from typing import Any, Optional
# from forest import metrics
# from forest import tree_exceptions


@dataclass
class ANode:
    """AVL Tree node definition."""
    key: Any
    data: Any
    left: Optional["ANode"] = None
    right: Optional["ANode"] = None
    parent: Optional["ANode"] = None
    height: int = 0


class AVLTree:
    """
    It is a typical AVL Tree.
    Attributes
    ----------
    root: `Optional[Node]`
        The root node of the AVL tree.
    empty: `bool`
        `True` if the tree is empty; `False` otherwise.
    Methods
    -------
    Core Functions
    search(key: `Any`)
        Look for a node based on the given key.
    insert(key: `Any`, data: `Any`)
        Insert a (key, data) pair into an AVL tree.
    delete(key: `Any`)
        Delete a node based on the given key from the AVL tree.
    Auxiliary Functions
    get_leftmost(node: `Node`)
        Return the node whose key is the smallest from the given subtree.
    get_rightmost(node: `Node` = `None`)
        Return the node whose key is the biggest from the given subtree.
    get_successor(node: `Node`)
        Return the successor node in the in-order order.
    get_predecessor(node: `Node`)
        Return the predecessor node in the in-order order.
    get_height(node: `Union[Node, Leaf]`)
        Return the height of the given node.
    """
    # def __init__(self, registry: Optional[metrics.MetricRegistry] = None) -> None:
    def __init__(self, registry: Optional[MetricRegistry] = None) -> None:
        # self.root: Optional[Node] = None
        self.root: Optional[ANode] = None
        self._metrics_enabled = True if registry else False
        if self._metrics_enabled and registry:
            # self._rotate_counter = metrics.Counter()
            self._rotate_counter = Counter()
            # self._height_histogram = metrics.Histogram()
            self._height_histogram = Histogram()
            registry.register(name="avlt.rotate", metric=self._rotate_counter)
            registry.register(name="avlt.height", metric=self._height_histogram)
    def __repr__(self) -> str:
        # Provie the tree representation to visualize its layout.
        if self.root:
            return (
                f"{type(self)}, root={self.root}, "
                f"tree_height={str(self.get_height(self.root))}"
            )
        return "empty tree"
    @property
    def empty(self) -> bool:
        """
        bool: `True` if the tree is empty; `False` otherwise.
        Notes
        -----
        The property, `empty`, is read-only.
        """
        return self.root is None
    def search(self, key: Any) -> Optional[ANode]:
        """
        Look for a node by a given key.
        Parameters
        key: `Any`
            The key associated with the node.
        Returns
            `Optional[Node]`
            The node found by the given key.
        If the key does not exist, return `None`.
        """
        return self._search(key=key)
    def _search(self, key: Any) -> Optional[ANode]:
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:  # Key found
                return current
        return None
    def insert(self, key: Any, data: Any) -> None:
        """
        Insert a (key, data) pair into the AVL tree.
        Parameters
        key: `Any`
            The key associated with the data.
        data: `Any`
            The data to be inserted.
        Raises
            `DuplicateKeyError`
            Raised if the key to be insted has existed in the tree.
        """
        new_node = ANode(key=key, data=data)
        parent: Optional[ANode] = None
        current: Optional[ANode] = self.root
        while current:
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                # raise tree_exceptions.DuplicateKeyError(key=new_node.key)
                raise DuplicateKeyError(key=new_node.key)
        new_node.parent = parent
        # If the tree is empty, set the new node to be the root.
        if parent is None:
            self.root = new_node
        else:
            if new_node.key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
            # After the insertion, fix the broken AVL-tree-property.
            # If the parent has two children after inserting the new node,
            # it means the parent had one child before the insertion.
            # In this case, neither AVL-tree property breaks nor
            # heights update requires.
            if not (parent.left and parent.right):
                self._insert_fixup(new_node)
        if self._metrics_enabled:
            self._height_histogram.update(value=self.get_height(self.root))
    def delete(self, key: Any) -> None:
        """
        Delete a node according to the given key.
        Parameters
        key: `Any`
            The key of the node to be deleted.
        """
        # for Python 3.9 and above 
        if self.root and (deleting_node := self._search(key=key)):
            # Case: no child
            if (deleting_node.left is None) and (deleting_node.right is None):
                self._delete_no_child(deleting_node=deleting_node)
            # Case: Two children
            elif deleting_node.left and deleting_node.right:
                replacing_node = self.get_leftmost(node=deleting_node.right)
                # Replace the deleting node with the replacing node,
                # but keep the replacing node in place.
                deleting_node.key = replacing_node.key
                deleting_node.data = replacing_node.data
                if replacing_node.right:  # The replacing node cannot have left child.
                    self._delete_one_child(deleting_node=replacing_node)
                else:
                    self._delete_no_child(deleting_node=replacing_node)
            # Case: one child
            else:
                self._delete_one_child(deleting_node=deleting_node)
            if self._metrics_enabled:
                self._height_histogram.update(value=self.get_height(self.root))
    @staticmethod
    def get_leftmost(node: ANode) -> ANode:
        """
        Return the leftmost node from a given subtree.
        The key of the leftmost node is the smallest key in the given subtree.
        Parameters
        node: `Node`
            The root of the subtree.
        Returns
        `Node`
            The node whose key is the smallest from the subtree of
            the given node.
        """
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node
    @staticmethod
    def get_rightmost(node: ANode) -> ANode:
        """
        Return the rightmost node from a given subtree.
        The key of the rightmost node is the biggest key in the given subtree.
        Parameters
        node: `Node`
            The root of the subtree.
        Return
            `Node`
            The node whose key is the biggest from the subtree of
            the given node.
        """
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node
    @staticmethod
    def get_successor(node: ANode) -> Optional[ANode]:
        """
        Return the successor in the in-order order.
        Parameters
        node: `Node`
            The node to get its successor.
        Return
            `Optional[Node]`
            The successor node.
        """
        if node.right:  # Case 1: right child is not empty
            # return AVLTree.get_leftmost(node=node.right)
            return self.get_leftmost(node=node.right)
        # Case 2: right child is empty
        parent = node.parent
        while parent and (node == parent.right):
            node = parent
            parent = parent.parent
        return parent
    @staticmethod
    def get_predecessor(node: ANode) -> Optional[ANode]:
        """
        Return the predecessor in the in-order order.
        Parameters
        node: `Node`
            The node to get its predecessor.
        Returns
            `Optional[Node]`
            The predecessor node.
        """
        if node.left:  # Case 1: left child is not empty
            # return AVLTree.get_rightmost(node=node.left)
            return self.get_rightmost(node=node.left)
        # Case 2: left child is empty
        parent = node.parent
        while parent and (node == parent.left):
            node = parent
            parent = parent.parent
        return parent
    @staticmethod
    def get_height(node: Optional[ANode]) -> int:
        """
        Get the height of the given subtree.
        Parameters
        node: `Node`
            The root of the subtree to get its height.
        Return
            `int`
            The height of the given subtree. 0 if the subtree has only one node.
        """
        if node:
            return node.height
        # None has height -1
        return -1
    def _get_balance_factor(self, node: Optional[ANode]) -> int:
        if node:
            return self.get_height(node.left) - self.get_height(node.right)
        # Empty node's height is -1
        return -1
    def _left_rotate(self, node_x: ANode) -> None:
        node_y = node_x.right  # Set node y
        if node_y:
            # Turn node y's subtree into node x's subtree
            node_x.right = node_y.left
            if node_y.left:
                node_y.left.parent = node_x
            node_y.parent = node_x.parent
            # If node's parent is a Leaf, node y becomes the new root.
            if node_x.parent is None:
                self.root = node_y
            # Otherwise, update node x's parent.
            elif node_x == node_x.parent.left:
                node_x.parent.left = node_y
            else:
                node_x.parent.right = node_y
            node_y.left = node_x
            node_x.parent = node_y
            node_x.height = 1 + max(
                self.get_height(node_x.left), self.get_height(node_x.right)
            )
            node_y.height = 1 + max(
                self.get_height(node_y.left), self.get_height(node_y.right)
            )
            if self._metrics_enabled:
                self._rotate_counter.increase()
    def _right_rotate(self, node_x: ANode) -> None:
        node_y = node_x.left  # Set node y
        if node_y:
            # Turn node y's subtree into node x's subtree
            node_x.left = node_y.right
            if node_y.right:
                node_y.right.parent = node_x
            node_y.parent = node_x.parent
            # If node's parent is a Leaf, node y becomes the new root.
            if node_x.parent is None:
                self.root = node_y
            # Otherwise, update node x's parent.
            elif node_x == node_x.parent.right:
                node_x.parent.right = node_y
            else:
                node_x.parent.left = node_y
            node_y.right = node_x
            node_x.parent = node_y
            node_x.height = 1 + max(
                self.get_height(node_x.left), self.get_height(node_x.right)
            )
            node_y.height = 1 + max(
                self.get_height(node_y.left), self.get_height(node_y.right)
            )
            if self._metrics_enabled:
                self._rotate_counter.increase()
    def _insert_fixup(self, new_node: ANode) -> None:
        parent = new_node.parent
        while parent:
            parent.height = 1 + max(
                self.get_height(parent.left), self.get_height(parent.right)
            )
            grandparent = parent.parent
            # grandparent is unbalanced
            if grandparent:
                if self._get_balance_factor(grandparent) > 1:
                    # Case Left-Left
                    if self._get_balance_factor(parent) >= 0:
                        self._right_rotate(grandparent)
                    # Case Left-Right
                    elif self._get_balance_factor(parent) < 0:
                        self._left_rotate(parent)
                        self._right_rotate(grandparent)
                    # Since the fixup does not affect the ancestor of the unbalanced
                    # node, exit the loop to complete the fixup process.
                    break
                elif self._get_balance_factor(grandparent) < -1:
                    # Case Right-Right
                    if self._get_balance_factor(parent) <= 0:
                        self._left_rotate(grandparent)
                    # Case Right-Left
                    elif self._get_balance_factor(parent) > 0:
                        self._right_rotate(parent)
                        self._left_rotate(grandparent)
                    # Since the fixup does not affect the ancestor of the unbalanced
                    # node, exit the loop to complete the fixup process.
                    break
            parent = parent.parent
    def _delete_no_child(self, deleting_node: ANode) -> None:
        parent = deleting_node.parent
        self._transplant(deleting_node=deleting_node, replacing_node=None)
        if parent:
            self._delete_fixup(fixing_node=parent)
    def _delete_one_child(self, deleting_node: ANode) -> None:
        parent = deleting_node.parent
        replacing_node = (
            deleting_node.right if deleting_node.right else deleting_node.left
        )
        self._transplant(deleting_node=deleting_node, replacing_node=replacing_node)
        if parent:
            self._delete_fixup(fixing_node=parent)
    def _transplant(self, deleting_node: ANode, replacing_node: Optional[ANode]) -> None:
        if deleting_node.parent is None:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node
        if replacing_node:
            replacing_node.parent = deleting_node.parent
    def _delete_fixup(self, fixing_node: ANode) -> None:
        while fixing_node:
            fixing_node.height = 1 + max(
                self.get_height(fixing_node.left), self.get_height(fixing_node.right)
            )
            if self._get_balance_factor(fixing_node) > 1:
                # Case Left-Left
                if self._get_balance_factor(fixing_node.left) >= 0:
                    self._right_rotate(fixing_node)
                # Case Left-Right
                elif self._get_balance_factor(fixing_node.left) < 0:
                    # The fixing node's left child cannot be empty
                    self._left_rotate(fixing_node.left)  # type: ignore
                    self._right_rotate(fixing_node)
            elif self._get_balance_factor(fixing_node) < -1:
                # Case Right-Right
                if self._get_balance_factor(fixing_node.right) <= 0:
                    self._left_rotate(fixing_node)
                # Case Right-Left
                elif self._get_balance_factor(fixing_node.right) > 0:
                    # The fixing node's right child cannot be empty
                    self._right_rotate(fixing_node.right)  # type: ignore
                    self._left_rotate(fixing_node)
            fixing_node = fixing_node.parent  # type: ignore

##########################################################################################################


# 4. binary_search_tree.py


import dataclasses
from typing import Any, Optional

# from forest import metrics
# from forest import tree_exceptions


@dataclasses.dataclass
class BNode:
    """Binary Search Tree node definition. B means BST"""
    key: Any
    data: Any
    left: Optional["BNode"] = None
    right: Optional["BNode"] = None
    parent: Optional["BNode"] = None


class BinarySearchTree:
    """
    Attributes
    ----------
    root: `Optional[Node]`
        The root node of the binary search tree.
    empty: `bool`
        `True` if the tree is empty; `False` otherwise.
    Methods
    -------
    Core Functions
    search(key: `Any`)
        Look for a node based on the given key.
    insert(key: `Any`, data: `Any`)
        Insert a (key, data) pair into a binary tree.
    delete(key: `Any`)
        Delete a node based on the given key from the binary tree.
    Auxiliary Functions
    get_leftmost(node: `Node`)
        Return the node whose key is the smallest from the given subtree.
    get_rightmost(node: `Node` = `None`)
        Return the node whose key is the biggest from the given subtree.
    get_successor(node: `Node`)
        Return the successor node in the in-order order.
    get_predecessor(node: `Node`)
        Return the predecessor node in the in-order order.
    get_height(node: `Optional[Node]`)
        Return the height of the given node.
    """
    # def __init__(self, registry: Optional[metrics.MetricRegistry] = None) -> None:
    def __init__(self, registry: Optional[MetricRegistry] = None) -> None:
        self.root: Optional[BNode] = None
        self._metrics_enabled = True if registry else False
        if self._metrics_enabled and registry:
            # self._height_histogram = metrics.Histogram()
            self._height_histogram = Histogram()
            registry.register(name="bst.height", metric=self._height_histogram)
    def __repr__(self) -> str:
        """Provide the tree representation to visualize its layout."""
        if self.root:
            return (
                f"{type(self)}, root={self.root}, "
                f"tree_height={str(self.get_height(self.root))}"
            )
        return "empty tree"
    @property
    def empty(self) -> bool:
        """
        bool: `True` if the tree is empty; `False` otherwise.
        Notes
        The property, `empty`, is read-only.
        """
        return self.root is None
    def search(self, key: Any) -> Optional[BNode]:
        """
        Look for a node by a given key.
        Parameters
        key: `Any`
            The key associated with the node.
        Return
            `Optional[Node]`
            The node found by the given key.
            If the key does not exist, return `None`.
        """
        return self._search(key=key)
    def _search(self, key: Any) -> Optional[BNode]:
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current
        return None
    def insert(self, key: Any, data: Any) -> None:
        """
        Insert a (key, data) pair into the binary search tree.
        Parameters
        key: `Any`
            The key associated with the data.
        data: `Any`
            The data to be inserted.
        Raises
            `DuplicateKeyError`
            Raised if the key to be insted has existed in the tree.
        """
        new_node = BNode(key=key, data=data)
        parent: Optional[BNode] = None
        current: Optional[BNode] = self.root
        while current:
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                # raise tree_exceptions.DuplicateKeyError(key=new_node.key)
                raise DuplicateKeyError(key=new_node.key)
        new_node.parent = parent
        # If the tree is empty
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        if self._metrics_enabled and self.root:
            self._height_histogram.update(value=self.get_height(self.root))
    def delete(self, key: Any) -> None:
        """
        Delete a node according to the given key.
        Parameters
        key: `Any`
            The key of the node to be deleted.
        """
        if self.root and (deleting_node := self._search(key=key)):
            # Case 1: no child or Case 2a: only one right child
            if deleting_node.left is None:
                self._transplant(
                    deleting_node=deleting_node, replacing_node=deleting_node.right
                )
            # Case 2b: only one left left child
            elif deleting_node.right is None:
                self._transplant(
                    deleting_node=deleting_node, replacing_node=deleting_node.left
                )
            # Case 3: two children
            else:
                replacing_node = BinarySearchTree.get_leftmost(node=deleting_node.right)
                # replacing_node = self.get_leftmost(node=deleting_node.right)
                # The leftmost node is not the direct child of the deleting node
                if replacing_node.parent != deleting_node:
                    self._transplant(
                        deleting_node=replacing_node,
                        replacing_node=replacing_node.right,
                    )
                    replacing_node.right = deleting_node.right
                    replacing_node.right.parent = replacing_node
                self._transplant(
                    deleting_node=deleting_node, replacing_node=replacing_node
                )
                replacing_node.left = deleting_node.left
                replacing_node.left.parent = replacing_node
            if self._metrics_enabled and self.root:
                self._height_histogram.update(value=self.get_height(self.root))
    @staticmethod
    def get_leftmost(node: BNode) -> BNode:
        """
        Return the leftmost node from a given subtree.
        The key of the leftmost node is the smallest key in the given subtree.
        Parameters
        node: `Node`
            The root of the subtree.
        Returns
            `Node`
            The node whose key is the smallest from the subtree of
            the given node.
        """
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node
    @staticmethod
    def get_rightmost(node: BNode) -> BNode:
        """
        Return the rightmost node from a given subtree.
        The key of the rightmost node is the biggest key in the given subtree.
        Parameters
        node: `Node`
            The root of the subtree.
        Returns
            `Node`
            The node whose key is the biggest from the subtree of
            the given node.
        """
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node
    @staticmethod
    def get_successor(node: BNode) -> Optional[BNode]:
        """
        Return the successor in the in-order order.
        Parameters
        node: `Node`
            The node to get its successor.
        Returns
            `Optional[Node]`
            The successor node.
        """
        if node.right:  # Case 1: right child is not empty
            return BinarySearchTree.get_leftmost(node=node.right)
            # return self.get_leftmost(node=node.right)
        # Case 2: right child is empty
        parent = node.parent
        while parent and (node == parent.right):
            node = parent
            parent = parent.parent
        return parent
    @staticmethod
    def get_predecessor(node: BNode) -> Optional[BNode]:
        """
        Return the predecessor in the in-order order.
        Parameters
        node: `Node`
            The node to get its predecessor.
        Returns
            `Optional[Node]`
            The predecessor node.
        """
        if node.left:  # Case 1: left child is not empty
            return BinarySearchTree.get_rightmost(node=node.left)
            # return self.get_rightmost(node=node.left)
        # Case 2: left child is empty
        parent = node.parent
        while parent and (node == parent.left):
            node = parent
            parent = parent.parent
        return parent
    @staticmethod
    def get_height(node: BNode) -> int:
        """
        Get the height of the given subtree.
        Parameters
        node: `Node`
            The root of the subtree to get its height.
        Returns
            `int`
            The height of the given subtree. 0 if the subtree has only one node.
        """
        if node.left and node.right:
            return (
                max(
                    BinarySearchTree.get_height(node=node.left),
                    # self.get_height(node=node.left),
                    BinarySearchTree.get_height(node=node.right),
                    # self.get_height(node=node.right),
                )
                + 1
            )
        if node.left:
            return BinarySearchTree.get_height(node=node.left) + 1
            # return self.get_height(node=node.left) + 1
        if node.right:
            return BinarySearchTree.get_height(node=node.right) + 1
            # return self.get_height(node=node.right) + 1
        # If reach here, it means the node is a leaf node.
        return 0
    def _transplant(self, deleting_node: BNode, replacing_node: Optional[BNode]) -> None:
        if deleting_node.parent is None:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node
        if replacing_node:
            replacing_node.parent = deleting_node.parent

##########################################################################################################


# 5. traversal.py


"""
Traversal module for traversing binary trees.
"""


from typing import Any, Iterator, Union
# from forest.binary_trees import binary_search_tree
# from forest.binary_trees import avl_tree


# SupportedNode = Union[None, binary_search_tree.Node, avl_tree.Node]
SupportedNode = Union[None, BNode, ANode]
# SupportedTree = Union[binary_search_tree.BinarySearchTree, avl_tree.AVLTree]
SupportedTree = Union[BinarySearchTree, AVLTree]


Pairs = Iterator[tuple[Any, Any]]


def inorder_traverse(tree: SupportedTree, recursive: bool = True) -> Pairs:
    """
    Perform In-Order traversal.
    In-order traversal traverses a tree by the order:
    left subtree, current node, right subtree (LDR)
    Parameters
    tree : `SupportedTree`
        An instance of the supported binary tree types.
    recursive: `bool`
        Perform traversal recursively or not.
    Yields
    `Pairs`
        The next (key, data) pair in the in-order traversal.
    Examples
    >>> from forest.binary_trees import binary_search_tree
    >>> from forest.binary_trees import traversal
    >>> tree = binary_search_tree.BinarySearchTree()
    >>> tree.insert(key=23, data="23")
    >>> tree.insert(key=4, data="4")
    >>> tree.insert(key=30, data="30")
    >>> tree.insert(key=11, data="11")
    >>> tree.insert(key=7, data="7")
    >>> tree.insert(key=34, data="34")
    >>> tree.insert(key=20, data="20")
    >>> tree.insert(key=24, data="24")
    >>> tree.insert(key=22, data="22")
    >>> tree.insert(key=15, data="15")
    >>> tree.insert(key=1, data="1")
    >>> [item for item in traversal.inorder_traverse(tree)]
    [(1, '1'), (4, '4'), (7, '7'), (11, '11'), (15, '15'), (20, '20'),
     (22, '22'), (23, '23'), (24, '24'), (30, '30'), (34, '34')]
    """
    if recursive:
        return _inorder_traverse(node=tree.root)
    return _inorder_traverse_non_recursive(root=tree.root)


def preorder_traverse(tree: SupportedTree, recursive: bool = True) -> Pairs:
    """
    Perform Pre-Order traversal.
    Pre-order traversal traverses a tree by the order:
    current node, left subtree, right subtree (DLR)
    Parameters
    tree : `SupportedTree`
        An instance of the supported binary tree types.
    recursive: `bool`
        Perform traversal recursively or not.
    Yields
    `Pairs`
        The next (key, data) pair in the pre-order traversal.
    Examples
    --------
    >>> from forest.binary_trees import binary_search_tree
    >>> from forest.binary_trees import traversal
    >>> tree = binary_search_tree.BinarySearchTree()
    >>> tree.insert(key=23, data="23")
    >>> tree.insert(key=4, data="4")
    >>> tree.insert(key=30, data="30")
    >>> tree.insert(key=11, data="11")
    >>> tree.insert(key=7, data="7")
    >>> tree.insert(key=34, data="34")
    >>> tree.insert(key=20, data="20")
    >>> tree.insert(key=24, data="24")
    >>> tree.insert(key=22, data="22")
    >>> tree.insert(key=15, data="15")
    >>> tree.insert(key=1, data="1")
    >>> [item for item in traversal.preorder_traverse(tree)]
    [(23, '23'), (4, '4'), (1, '1'), (11, '11'), (7, '7'), (20, '20'),
     (15, '15'), (22, '22'), (30, '30'), (24, '24'), (34, '34')]
    """
    if recursive:
        return _preorder_traverse(node=tree.root)
    return _preorder_traverse_non_recursive(root=tree.root)


def postorder_traverse(tree: SupportedTree, recursive: bool = True) -> Pairs:
    """
    Perform Post-Order traversal.
    Post-order traversal traverses a tree by the order:
    left subtree, right subtree, current node (LRD)
    Parameters
    tree : `SupportedTree`
        An instance of the supported binary tree types.
    recursive: `bool`
        Perform traversal recursively or not.
    Yields
    `Pairs`
        The next (key, data) pair in the post-order traversal.
    Examples
    >>> from forest.binary_trees import binary_search_tree
    >>> from forest.binary_trees import traversal
    >>> tree = binary_search_tree.BinarySearchTree()
    >>> tree.insert(key=23, data="23")
    >>> tree.insert(key=4, data="4")
    >>> tree.insert(key=30, data="30")
    >>> tree.insert(key=11, data="11")
    >>> tree.insert(key=7, data="7")
    >>> tree.insert(key=34, data="34")
    >>> tree.insert(key=20, data="20")
    >>> tree.insert(key=24, data="24")
    >>> tree.insert(key=22, data="22")
    >>> tree.insert(key=15, data="15")
    >>> tree.insert(key=1, data="1")
    >>> [item for item in traversal.postorder_traverse(tree)]
    [(1, '1'), (7, '7'), (15, '15'), (22, '22'), (20, '20'), (11, '11'),
     (4, '4'), (24, '24'), (34, '34'), (30, '30'), (23, '23')]
    """
    if recursive:
        return _postorder_traverse(node=tree.root)
    return _postorder_traverse_non_recursive(root=tree.root)


def reverse_inorder_traverse(tree: SupportedTree, recursive: bool = True) -> Pairs:
    """
    Perform reversed In-Order traversal.
    Reversed in-order traversal traverses a tree by the order:
    right subtree, current node, left subtree (RNL)
    Parameters
    tree : `SupportedTree`
        An instance of the supported binary tree types.
    recursive: `bool`
        Perform traversal recursively or not.
    Yields
    `Pairs`
        The next (key, data) pair in the reversed in-order traversal.
    Examples
    >>> from forest.binary_trees import binary_search_tree
    >>> from forest.binary_trees import traversal
    >>> tree = binary_search_tree.BinarySearchTree()
    >>> tree.insert(key=23, data="23")
    >>> tree.insert(key=4, data="4")
    >>> tree.insert(key=30, data="30")
    >>> tree.insert(key=11, data="11")
    >>> tree.insert(key=7, data="7")
    >>> tree.insert(key=34, data="34")
    >>> tree.insert(key=20, data="20")
    >>> tree.insert(key=24, data="24")
    >>> tree.insert(key=22, data="22")
    >>> tree.insert(key=15, data="15")
    >>> tree.insert(key=1, data="1")
    >>> [item for item in traversal.reverse_inorder_traverse(tree)]
    [(34, '34'), (30, '30'), (24, '24'), (23, '23'), (22, '22'), (20, '20'),
     (15, '15'), (11, '11'), (7, '7'), (4, '4'), (1, '1')]
    """
    if recursive:
        return _reverse_inorder_traverse(node=tree.root)
    return _reverse_inorder_traverse_non_recursive(root=tree.root)


def levelorder_traverse(tree: SupportedTree) -> Pairs:
    """
    Perform Level-Order traversal.
    Level-order traversal traverses a tree:
    level by level, from left to right, starting from the root node.
    Parameters
    tree : `SupportedTree`
        An instance of the supported binary tree types.
    Yields
    `Pairs`
        The next (key, data) pair in the level-order traversal.
    Examples
    >>> from forest.binary_trees import binary_search_tree
    >>> from forest.binary_trees import traversal
    >>> tree = binary_search_tree.BinarySearchTree()
    >>> tree.insert(key=23, data="23")
    >>> tree.insert(key=4, data="4")
    >>> tree.insert(key=30, data="30")
    >>> tree.insert(key=11, data="11")
    >>> tree.insert(key=7, data="7")
    >>> tree.insert(key=34, data="34")
    >>> tree.insert(key=20, data="20")
    >>> tree.insert(key=24, data="24")
    >>> tree.insert(key=22, data="22")
    >>> tree.insert(key=15, data="15")
    >>> tree.insert(key=1, data="1")
    >>> [item for item in traversal.levelorder_traverse(tree)]
    [(23, '23'), (4, '4'), (30, '30'), (1, '1'), (11, '11'), (24, '24'),
     (34, '34'), (7, '7'), (20, '20'), (15, '15'), (22, '22')]
    """
    queue = [tree.root]
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp:
            yield (temp.key, temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)


def _inorder_traverse(node: SupportedNode) -> Pairs:
    if node:
        yield from _inorder_traverse(node.left)
        yield (node.key, node.data)
        yield from _inorder_traverse(node.right)


def _inorder_traverse_non_recursive(root: SupportedNode) -> Pairs:
    if root is None:
        raise StopIteration
    stack = []
    if root.right:
        stack.append(root.right)
    stack.append(root)
    current = root.left
    while True:
        if current:
            if current.right:
                stack.append(current.right)
                stack.append(current)
                current = current.left
                continue
            stack.append(current)
            current = current.left
        else:  # current is None
            if len(stack) > 0:
                current = stack.pop()
                if current.right is None:
                    yield (current.key, current.data)
                    current = None
                    continue
                else:  # current.right is not None
                    if len(stack) > 0:
                        if current.right == stack[-1]:
                            yield (current.key, current.data)
                            current = stack.pop() if len(stack) > 0 else None
                            continue
                        else:  # current.right != stack[-1]:
                            # This case means there are more nodes on the right
                            # Keep the current and go back to add them.
                            continue
            else:  # stack is empty
                break


def _reverse_inorder_traverse(node: SupportedNode) -> Pairs:
    if node:
        yield from _reverse_inorder_traverse(node.right)
        yield (node.key, node.data)
        yield from _reverse_inorder_traverse(node.left)


def _reverse_inorder_traverse_non_recursive(root: SupportedNode) -> Pairs:
    if root is None:
        raise StopIteration
    stack = []
    if root.left:
        stack.append(root.left)
    stack.append(root)
    current = root.right
    while True:
        if current:
            if current.left:
                stack.append(current.left)
                stack.append(current)
                current = current.right
                continue
            stack.append(current)
            current = current.right
        else:  # current is None
            if len(stack) > 0:
                current = stack.pop()
                if current.left is None:
                    yield (current.key, current.data)
                    current = None
                    continue
                else:  # current.right is not None
                    if len(stack) > 0:
                        if current.left == stack[-1]:
                            yield (current.key, current.data)
                            current = stack.pop() if len(stack) > 0 else None
                            continue
                        else:  # current.right != stack[-1]:
                            # This case means there are more nodes on the right
                            # Keep the current and go back to add them.
                            continue
            else:  # stack is empty
                break


def _preorder_traverse(node: SupportedNode) -> Pairs:
    if node:
        yield (node.key, node.data)
        yield from _preorder_traverse(node.left)
        yield from _preorder_traverse(node.right)


def _preorder_traverse_non_recursive(root: SupportedNode) -> Pairs:
    if root is None:
        raise StopIteration
    stack = [root]
    while len(stack) > 0:
        temp = stack.pop()
        yield (temp.key, temp.data)
        # Because stack is FILO, insert right child before left child.
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)


def _postorder_traverse(node: SupportedNode) -> Pairs:
    if node:
        yield from _postorder_traverse(node.left)
        yield from _postorder_traverse(node.right)
        yield (node.key, node.data)


def _postorder_traverse_non_recursive(root: SupportedNode) -> Pairs:
    if root is None:
        raise StopIteration
    stack = []
    if root.right:
        stack.append(root.right)
    stack.append(root)
    current = root.left
    while True:
        if current:
            if current.right:
                stack.append(current.right)
                stack.append(current)
                current = current.left
                continue
            else:  # current.right is None
                if current.left:
                    stack.append(current)
                else:
                    yield (current.key, current.data)
                current = current.left
        else:  # current is None
            if len(stack) > 0:
                current = stack.pop()
                if current.right is None:
                    yield (current.key, current.data)
                    current = None
                else:  # current.right is not None
                    if len(stack) > 0:
                        if current.right != stack[-1]:
                            yield (current.key, current.data)
                            current = None
                        else:  # current.right == stack[-1]
                            temp = stack.pop()
                            stack.append(current)
                            current = temp
                    else:  # stack is empty
                        yield (current.key, current.data)
                        break
            else:  # stack is empty
                break

##########################################################################################################


# 6. avl_map.py

# Example: It is the exmaple to call the above scripts. 


from typing import Any, Optional
# from forest.binary_trees import avl_tree
# from forest.binary_trees import traversal


class Map:
    """Key-value Map implemented using AVL Tree."""
    def __init__(self) -> None:
        # self._avlt = avl_tree.AVLTree()
        self._avlt = AVLTree()
    def __setitem__(self, key: Any, value: Any) -> None:
        # Insert (key, value) item into the map.
        self._avlt.insert(key=key, data=value)
    def __getitem__(self, key: Any) -> Optional[Any]:
        # Get the data by the given key.
        node = self._avlt.search(key=key)
        if node:
            return node.data
        return None
    def __delitem__(self, key: Any) -> None:
        # Remove a (key, value) pair from the map.
        self._avlt.delete(key=key)
    # def __iter__(self) -> traversal.Pairs:
    def __iter__(self) -> Pairs:
        # Iterate the data in the map.
        # return traversal.inorder_traverse(tree=self._avlt)
        return inorder_traverse(tree=self._avlt)
    @property
    def empty(self) -> bool:
        # Return `True` if the map is empty; `False` otherwise.
        return self._avlt.empty


if __name__ == "__main__":
    # Initialize the Map instance.
    contacts = Map()
    # Add some items.
    contacts["Mark"] = "mark@gmail.com"
    contacts["John"] = "john@hotmail.com"
    contacts["Luke"] = "luke@yahoo.com"
    # Retrieve an email
    print(contacts["Mark"])
    # Delete one item.
    del contacts["John"]
    # Check the deleted item.
    print(contacts["John"])  # This will print None
    # Iterate the items.
    for contact in contacts:
        print(contact)


# Output:

"""
mark@gmail.com
None
('Luke', 'luke@yahoo.com')
('Mark', 'mark@gmail.com')
"""

#######################################################################################


# 7. bst_vs_avl.py 


# It is the comparison between BST and AVLTree. 


import random


insert_data = random.sample(range(1, 2000), 1000)
delete_data = random.sample(insert_data, 1000)

registry = MetricRegistry()
bstree = BinarySearchTree(registry=registry)
avltree = AVLTree(registry=registry)


for key in insert_data:
    bstree.insert(key=key, data=str(key))
    avltree.insert(key=key, data=str(key))


for key in delete_data:
    bstree.delete(key=key)
    avltree.delete(key=key)

print("Binary Search Tree:")
bst_report = registry.get_metric(name="bst.height").report()  # type: ignore
print(f"  Height:   {bst_report}")

print("AVL Tree:")
avlt_rotation_count = registry.get_metric(name="avlt.rotate").count  # type: ignore
print(f"  Rotation: {avlt_rotation_count}")
avlt_report = registry.get_metric(name="avlt.height").report()  # type: ignore
print(f"  Height:   {avlt_report}")


# Output:

"""
Binary Search Tree:
Height:   {'min': 0, 'max': 18, 'medium': 17.0, 'mean': 15.887443721860931, 'stdDev': 2.6367240233852884, 'percentile': {'75': 18.0, '95': 18.0, '99': 18.0}}
AVL Tree:
  Rotation: 1127
Height:   {'min': -1, 'max': 11, 'medium': 10.0, 'mean': 9.136, 'stdDev': 1.6936658466179213, 'percentile': {'75': 10.0, '95': 11.0, '99': 11.0}}
"""
from typing import Optional


class BinarySearchTree:
    class Node:
        def __init__(self, key: object, val: object):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.size = 1

    def __init__(self, root: Node = None):
        self.root = root

    def size(self):
        return self.__size(self.root)

    @staticmethod
    def __size(x: Node):
        return 0 if x is None else x.size

    def get(self, key: object) -> object:
        return self.__get(self.root, key)

    def __get(self, x: Node, key: object) -> object:
        if x is None:
            return None
        if x.key > key:
            return self.__get(x.left, key)
        elif x.key < key:
            return self.__get(x.right, key)
        else:
            return x

    def put(self, key: object, val: object):
        self.root = self.__put(self.root, key, val)
        return self

    def __put(self, x: Node, key: object, val: object):
        if x is None:
            return self.Node(key, val)
        elif x.key > key:
            x.left = self.__put(x.left, key, val)
        elif x.key < key:
            x.right = self.__put(x.right, key, val)
        else:
            x.val = val
        x.size = self.__size(x.left) + self.__size(x.right) + 1
        return x

    def floor(self, key: object) -> object:
        node = self.__floor(self.root, key)
        if node is None:
            raise Exception("key not found", key)
        return node.key

    def __floor(self, x: Node, key: object) -> Optional[Node]:
        if x is None:
            return None
        if x.key == key:
            return x
        if x.key > key:
            return self.__floor(x.left, key)
        t = self.__floor(x.right, key)
        return t if t is not None else x

    def min(self):
        if self.root is None:
            raise Exception("BST is empty")
        return self.__min(self.root).key

    def __min(self, x: Node) -> Node:
        return x if x.left is None else self.__min(x.left)

    def select(self, r: int) -> object:
        """
        Find a key for a given rank 'r', such that a key is greater than 'r' given keys
        :param r: rank of the node
        :return: key of the node
        """
        if r < 0 or r >= self.size():
            raise Exception(f"Invalid rank request: {r}")
        return self.__select(self.root, r).key

    def __select(self, node: Node, rank: int) -> Optional[Node]:
        if node is None:
            return None
        t = self.__size(node.left)
        if rank < t:
            # left subtree is bigger than the given rank, searching there
            return self.__select(node.left, rank)
        elif rank > t:
            # left subtree is smaller thank the given rank
            # searching for the residual rank in the right subtree
            return self.__select(node.right, rank - t - 1)
        else:
            return node

    def rank(self, key: object) -> int:
        return self.__rank(self.root, key)

    def __rank(self, node: Node, key: object) -> int:
        """
        Identifies the rank for the key. Rank is how many nodes are less then the node with that key.
        :param node: starting node
        :param key: given key
        :return: rank, number of nodes smaller than the node with the given key
        """
        if node is None:
            return 0
        if key < node.key:
            # key is smaller then the current one, look in the left subtree
            return self.__rank(node.left, key)
        elif key > node.key:
            # key is greater than the current node's key
            # we add up current node's rank (left subtree size), the root (1) and key's rank in the right subtree
            return 1 + self.__size(node.left) + self.__rank(node.right, key)
        else:
            # the key is equal to the current node's key, so the rank is the size of the left subtree
            return self.__size(node.left)


def test_base_operations():
    bst = init_bst()
    assert bst.root.size is 4
    assert bst.root.key is "h"
    assert bst.root.val is 1
    assert bst.root.right.key is "y"
    assert bst.root.right.val is 5
    assert bst.root.left.key is "b"
    assert bst.root.left.val is 2


def test_floor():
    bst = init_bst()
    assert bst.floor("d") == "b"
    assert bst.floor("z") == "y"
    assert bst.floor("x") == "h"
    assert bst.min() is "b"


def test_select():
    bst = init_bst()
    assert bst.select(0) == "b"
    assert bst.select(2) == "h"
    assert bst.select(3) == "y"


def test_rank():
    bst = init_bst()
    assert bst.rank("b") == 0
    assert bst.rank("h") == 2
    assert bst.rank("y") == 3


def init_bst():
    return BinarySearchTree().put("h", 1).put("b", 2).put("e", 3).put("y", 5)

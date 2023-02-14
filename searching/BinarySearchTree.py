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


def test_op():
    bst = BinarySearchTree()
    bst.put("h", 1)
    bst.put("b", 2)
    bst.put("e", 3)
    bst.put("y", 5)

    assert bst.root.size is 4
    assert bst.root.key is "h"
    assert bst.root.val is 1
    assert bst.root.right.key is "y"
    assert bst.root.right.val is 5
    assert bst.root.left.key is "b"
    assert bst.root.left.val is 2

    assert bst.floor("d") == "b"
    assert bst.floor("z") == "y"
    assert bst.floor("x") == "h"

    assert bst.min() is "b"

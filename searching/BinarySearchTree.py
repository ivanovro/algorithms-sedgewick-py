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
        return self.size_of_node(self.root)

    @staticmethod
    def size_of_node(node: Node):
        return 0 if node is None else node.size

    def get(self, key: object) -> object:
        return self.get_value(self.root, key)

    def get_value(self, node: Node, key: object) -> object:
        if node is None:
            return None
        if node.key > key:
            return self.get_value(node.left, key)
        elif node.key < key:
            return self.get_value(node.right, key)
        else:
            return node

    def put(self, key: object, val: object):
        self.root = self.put_value(self.root, key, val)

    def put_value(self, node: Node, key: object, val: object):
        if node is None:
            return self.Node(key, val)
        elif node.key > key:
            node.left = self.put_value(node.left, key, val)
        elif node.key < key:
            node.right = self.put_value(node.right, key, val)
        else:
            node.val = val
        node.size = self.size_of_node(node.left) + self.size_of_node(node.right) + 1
        return node


def test_put():
    bst = BinarySearchTree()
    bst.put("h", 1)
    bst.put("b", 2)
    bst.put("c", 3)
    bst.put("y", 5)
    assert bst.root.size is 4
    assert bst.root.key is "h"
    assert bst.root.val is 1
    assert bst.root.right.key is "y"
    assert bst.root.right.val is 5
    assert bst.root.left.key is "b"
    assert bst.root.left.val is 2

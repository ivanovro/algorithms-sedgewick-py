from adt.LinkedListStack import Stack
from adt.Node import Node


def reverse(node: Node) -> Node:
    first, _ = reverse_node(node)
    return first


def reverse_node(node: Node) -> (Node, Node):
    if node.next is None:
        return node, node
    first, rev = reverse_node(node.next)
    rev.next = node
    node.next = None
    return first, node


def test_reverse():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    rev = reverse(stack.first)
    assert rev.item == 1
    assert rev.next.item == 2
    assert rev.next.next.item == 3

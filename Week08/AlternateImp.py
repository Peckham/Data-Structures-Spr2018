# Alternate Implementation of functions from LinkedBinaryTree.copyright
from functools import reduce
"""
Base case: we reach the end of a branch and the nodes are the same.
If, as we are recursing, we run into two different nodes, then
we return false.
Steps: Compare node. If nodes are different, return false.
Else, return the boolean value of the left recursion and right
recursion. The AND statement is the most important, tieing together
this recursion.
"""


def sameRecurse(self, other, node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1.element() != node2.element():
        return False
    else:
        return self.sameRecurse(other, self.left(node1),
                                other.left(node2)) and \
                                self.sameRecurse(other, self.right(node1),
                                                 other.right(node2))


def sum_of_leaves(self):
    # Problem 4
    isLeaf = filter(lambda w: self.is_leaf(w), self.positions())
    leafElts = map(lambda x: x.element(), isLeaf)
    return reduce((lambda y, z: y + z), leafElts)

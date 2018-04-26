import random

class Empty(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class SingleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node

    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linkedlist."""
        return self._size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        return self._size == 0

    def top(self):
        """Return (but do not remove) the element at the top of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._element              # head of list

    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        # Create a new link node and link it
        new_node = self._Node(e, self._head)
        self._head = new_node
        self._size += 1

    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        to_return = self._head._element
        self._head = self._head._next
        self._size -= 1
        return to_return

    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + "-->")
            curNode = curNode._next
        result.append("None")
        return "".join(result)


def merge_two_sorted_linked_lists(l1, l2):
    ''' Merges two **sorted** SingleLinkedLists l1 and l2.
        return a new merged, **sorted** SingleLinkedList.
        Assume l1, l2 are not empty.

        @l1 the first sorted SingleLinkedList
        @l2 the second sorted SingleLinkedList

        return the merged sorted linked list.
        For example:

        l1 is 1-->66-->73-->74-->95-->None
        l2 is 10-->48-->61-->78-->92-->None
        merge_two_sorted_linked_lists(l1, l2) should return:

        1-->10-->48-->61-->66-->73-->74-->78-->92-->95-->None

    '''

    # TODO
    newList = SingleLinkedList()
    curNode1 = l1.top()
    curNode2 = l2.top()
    while not l1.is_empty() and not l2.is_empty():
        if curNode1 < curNode2:
            newList.insert_from_head(l1.delete_from_head())
            if not l1.is_empty:
                curNode1 = l1.top()
            else:
                break
        else:
            newList.insert_from_head(l2.delete_from_head())
            if not l2.is_empty():
                curNode2 = l2.top()
            else:
                break
    while not l1.is_empty():
        newList.insert_from_head(l1.delete_from_head())
    while not l2.is_empty():
        newList.insert_from_head(l2.delete_from_head())
    return newList


def main():
    sample_list1 = SingleLinkedList()
    sample_list2 = SingleLinkedList()
    data1 = []
    data2 = []
    for i in range(5):
        data1.append(random.randint(0, 99))
        data2.append(random.randint(0, 99))
    data1.sort()
    data2.sort()
    for i in range(5):
        sample_list1.insert_from_head(data1[-i - 1])
        sample_list2.insert_from_head(data2[-i - 1])
    print("Before merging... l1 and l2 are:")
    print(sample_list1)
    print(sample_list2)
    answer = merge_two_sorted_linked_lists(sample_list1, sample_list2)
    print("After merging... Your returned list is:")
    print(answer)


main()

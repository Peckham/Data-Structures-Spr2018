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
        result.append("head --> ")
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + " --> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)


def union(l1, l2):
    ''' Return a new SingleLinkedList of the union of l1 and l2.
        Order of elements in output lists doesn’t matter.
        Use python built in dictionary for this question.
        @l1: the first SingleLinkedList
        @l2: the second SingleLinkedList

        return: union of l1 and l2, as a SingleLinkedList.
    '''
    # To do
    pass

def intersection(l1, l2):
    ''' Return a new SingleLinkedList of the intersection of l1 and l2.
        Order of elements in output lists doesn’t matter.
        Use python built in dictionary for this question.
        @l1: the first SingleLinkedList
        @l2: the second SingleLinkedList

        return: intersection of l1 and l2, as a SingleLinkedList.
    '''
    # To do
    pass


def main():
    l1 = SingleLinkedList()     # [10, 15, 4, 20]
    l1.insert_from_head(20)
    l1.insert_from_head(4)
    l1.insert_from_head(15)
    l1.insert_from_head(10)

    l2 = SingleLinkedList()     # [8, 4, 2, 10]
    l2.insert_from_head(10)
    l2.insert_from_head(2)
    l2.insert_from_head(4)
    l2.insert_from_head(8)

    print(union(l1, l2))
    print(intersection(l1, l2))

main()
    
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

    def __len__(self):
        """Return the number of elements in the linkedlist."""
        # TO DO #################
        size = 0
        curNode = self._head
        while curNode is not None:
            size += 1
            curNode = curNode._next
        return size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        return len(self) == 0

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

    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        to_return = self._head._element
        self._head = self._head._next
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


# Test code
lissy = SingleLinkedList()
for i in range(5):
    lissy.insert_from_head(i)
print(len(lissy))  # should print 5.

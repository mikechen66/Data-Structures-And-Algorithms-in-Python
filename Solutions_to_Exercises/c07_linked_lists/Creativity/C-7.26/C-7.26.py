# C-7.26
# Implement a method, concatenate(Q2) for the LinkedQueue class that
# takes all elements of LinkedQueue Q2 and appends them to the end of the
# original queue. The operation should run in O(1) time and should result
# in Q2 being an empty queue.


from exceptions_7_26 import Empty


# First, I modified the SinglyLinkedList class to include a tail attribute.
# It is used to access the end of the list without cycling through it.
# I also updated method to use this new tail attribute to improve speed.

# This is the new implementation:


###############################################################################
#               New implementation of the SinglyLinkedList class              #
###############################################################################
class SinglyLinkedList:
    """Singly linked list implementation"""

    # ----------------------- nested Node class ------------------------
    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Initialise the list with a header but it still has a size of zero"""
        self._header = self.Node(None, None)
        self.head = None
        self.tail = None
        self._size = 0

    # ----------------------- linked list methods ------------------------
    def add_first(self, e):
        """Adds e to the beginning of the list, after the header"""
        newest = self.Node(e, None)

        if self.is_empty():
            self.head = newest
            self.tail = newest
        else:
            newest._next = self.head
            self.head = newest

        self._header._next = newest
        self._size += 1

    def add_last(self, e):
        """Adds e to the end of the list"""
        newest = self.Node(e, None)

        if self.is_empty():
            self.head = newest
            self.tail = newest
            self._header._next = newest
        else:
            self.tail._next = newest
            self.tail = newest

        self._size += 1

    def remove_first(self):
        """Removes the first item of the list if it exists"""
        if self.is_empty():
            raise Empty("Cannot remove from an empty list.")

        head = self.head
        if self._size == 1:
            self.head = None
            self.tail = None
            self._header._next = None
        else:
            self.head = head._next
            self._header._next = self.head

        head._next = None                  # helps garbage collection
        self._size -= 1
        return head

    def remove_last(self):
        # This is an inefficient way to find the last element of the list,
        # it runs in O(n), but this is the only way to find it, because it is a singly linked list,
        # not a doubly linked list. This class is only for testing purposes anyway (small lists).

        """Removes the last item of the list if it exists"""
        if self.is_empty():
            raise Empty("Cannot remove from an empty list.")

        old_tail = self.tail
        if self._size == 1:
            self.head = None
            self.tail = None
            self._header._next = None
        else:
            new_tail = self._header
            while new_tail._next._next is not None:
                new_tail = new_tail._next
            new_tail._next = None
            self.tail = new_tail
        self._size -= 1
        return old_tail

    def get_head(self):
        """Returns the head element of the list"""
        if self.is_empty():
            raise Empty("Empty list does not have a head")
        return self.head

    def get_tail(self):
        """Finds and returns the tail element of the list"""
        if self.is_empty():
            raise Empty("Empty list does not have a tail")
        return self.tail

    def is_empty(self):
        """Returns True if empty"""
        return self._size == 0

    def get_size(self):
        """Returns the length of the list"""
        return self._size

    def __str__(self):
        """Printing the content of the list for visualisation and tests"""
        elements = []
        node = self._header
        while node._next is not None:  # for every node of the list besides _trailer
            node = node._next
            elements.append(str(node._element))
        return "[{}]".format(", ".join(elements))

    def __len__(self):
        """Enables len(SLL)"""
        return self._size


###############################################################################
#           Implementation of a queue from the SinglyLinkedList (7.26)        #
###############################################################################
class Queue_From_Singly_Linked_List(SinglyLinkedList):
    def __init__(self):
        self._data = SinglyLinkedList()

    def enqueue(self, e):
        """enqueue the item e"""
        self._data.add_last(e)

    def dequeue(self):
        """dequeue the first item enqueued"""
        if self.is_empty():
            raise Empty("Cannot dequeue from an empty queue")

        return self._data.remove_first()._element

    def first(self):
        """returns the first item in the queue"""
        if self.is_empty():
            raise Empty("Empty queue does not have a first element")
        return self._data.get_head()._element

    def is_empty(self):
        """returns True if the queue is empty"""
        return self._data.is_empty()

    def __len__(self):
        """returns the length of the queue"""
        return len(self._data)

    def __str__(self):
        return str(self._data)



###############################################################################
#                          Beginning of exercise 7.26                         #
###############################################################################
class LinkedQueueWithConcatenate(Queue_From_Singly_Linked_List):

    def concatenate(self, Q2):
        self._data.tail._next = Q2._data.get_head()
        self._data.tail = Q2._data.tail
        self._data._size += Q2._data._size

        Q2._data = SinglyLinkedList()    # Reset Q2


Q1 = LinkedQueueWithConcatenate()
Q2 = LinkedQueueWithConcatenate()

for i in range(4):
    Q1.enqueue(i)
    Q2.enqueue(i + 4)

print("Q1: ", Q1)
print("Q1 first is:", Q1.first())
print("Q2: ", Q2)
print("Q2 first is:", Q2.first())


print("Using concatenate method:")
Q1.concatenate(Q2)

print("Q1: ", Q1)
print("Q1 first is:", Q1.first())
print("Q2: ", Q2)

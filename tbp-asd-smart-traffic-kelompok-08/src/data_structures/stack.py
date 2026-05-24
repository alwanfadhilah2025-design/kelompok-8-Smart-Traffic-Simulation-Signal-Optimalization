from data_structures.linked_list import LLNode

class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):

        node = LLNode(data)
        node.next = self.top
        self.top = node

        self._size += 1

    def pop(self):

        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next

        self._size -= 1

        return data

    def peek(self):
        return self.top.data if self.top else None

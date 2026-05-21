class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def add_front(self, data):
        node = LLNode(data)
        node.next = self.head
        self.head = node
        self._size += 1

    def add_back(self, data):
        node = LLNode(data)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self._size += 1

    def find(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return curr.data
            curr = curr.next
        return None

    def delete_by_value(self, value):
        if not self.head:
            return False
        if self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return True
        curr = self.head
        while curr.next:
            if curr.next.data == value:
                curr.next = curr.next.next
                self._size -= 1
                return True
            curr = curr.next
        return False

    def __len__(self):
        return self._size

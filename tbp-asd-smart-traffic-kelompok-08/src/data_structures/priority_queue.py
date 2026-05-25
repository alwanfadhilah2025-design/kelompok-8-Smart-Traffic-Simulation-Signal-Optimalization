from data_structures.linked_list import LLNode

class PriorityQueueKendaraan:

    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, kendaraan):

        node = LLNode(kendaraan)

        if self.head is None:
            self.head = node

        elif kendaraan.jenis < self.head.data.jenis:
            node.next = self.head
            self.head = node

        else:
            curr = self.head

            while (
                curr.next and
                curr.next.data.jenis <= kendaraan.jenis
            ):
                curr = curr.next

            node.next = curr.next
            curr.next = node

        self._size += 1

    def dequeue(self):

        if self.head is None:
            return None

        data = self.head.data
        self.head = self.head.next
        self._size -= 1

        return data

    def __len__(self):
        return self._size

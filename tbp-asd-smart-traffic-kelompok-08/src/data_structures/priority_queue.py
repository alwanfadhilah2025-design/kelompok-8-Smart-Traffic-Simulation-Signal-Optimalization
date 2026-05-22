from .linked_list import LLNode

class PriorityQueueKendaraan:
    """Priority queue berdasarkan prioritas (nilai kecil = prioritas tinggi).
       Tie-break FIFO untuk prioritas sama."""
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, kendaraan):
        """O(n) insertion terurut berdasarkan prioritas (kendaraan.jenis)"""
        node = LLNode(kendaraan)

        if not self.head or kendaraan.jenis < self.head.data.jenis:
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            while curr.next and curr.next.data.jenis <= kendaraan.jenis:
                curr = curr.next
            node.next = curr.next
            curr.next = node
        self._size += 1

    def dequeue(self):
        """O(1) ambil elemen dengan prioritas tertinggi (paling depan)"""
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        self._size -= 1
        return val

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.head is None

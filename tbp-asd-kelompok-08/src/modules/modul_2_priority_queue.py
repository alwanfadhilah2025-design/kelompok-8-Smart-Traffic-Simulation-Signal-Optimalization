from dataclasses import dataclass

# Node untuk linked list (digunakan juga oleh stack)
class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

@dataclass
class Kendaraan:
    id_kendaraan: int
    jenis: int   # 1=AMBULANS (prioritas tertinggi), 2=BUS, 3=MOBIL, 4=MOTOR
    asal: str
    tujuan: str
    waktu_masuk: float

class PriorityQueueKendaraan:
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, kendaraan):
        """O(n) insertion terurut berdasarkan prioritas (jenis kecil = prioritas tinggi)"""
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
        """O(1)"""
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        self._size -= 1
        return val

    def __len__(self):
        return self._size

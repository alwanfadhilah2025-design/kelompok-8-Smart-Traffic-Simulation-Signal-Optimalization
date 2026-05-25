from data_structures.priority_queue import PriorityQueueKendaraan

class Kendaraan:

    def __init__(self, jenis):
        self.jenis = jenis

pq = PriorityQueueKendaraan()

pq.enqueue(Kendaraan(4))   # motor
pq.enqueue(Kendaraan(3))   # mobil
pq.enqueue(Kendaraan(1))   # ambulans

keluar = pq.dequeue()

print("Prioritas keluar:", keluar.jenis)

assert keluar.jenis == 1

print("TEST PRIORITY QUEUE BERHASIL")

import numpy as np, time, random
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple

np.random.seed(17)
random.seed(17)

ARAH = ['UTARA', 'SELATAN', 'TIMUR', 'BARAT']
JENIS_KENDARAAN = {'AMBULANS': 1, 'BUS': 2, 'MOBIL': 3, 'MOTOR': 4}

# ================= DATA =================
@dataclass
class Kendaraan:
    id_kendaraan: int
    jenis: int
    asal: str
    tujuan: str
    waktu_masuk: float

@dataclass
class Persimpangan:
    nama: str
    kapasitas: int = 20

# ================= LINKED LIST =================
class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# ================= PRIORITY QUEUE =================
class PriorityQueueKendaraan:
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, kendaraan):
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
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        self._size -= 1
        return val

    def __len__(self):
        return self._size

# ================= STACK =================
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
        if not self.top:
            return None
        val = self.top.data
        self.top = self.top.next
        self._size -= 1
        return val

    def peek(self):
        return self.top.data if self.top else None

# ================= GRAPH =================
class EdgeNode:
    def __init__(self, dest, jarak, kapasitas_lajur):
        self.dest = dest
        self.jarak = jarak
        self.kapasitas_lajur = kapasitas_lajur
        self.next = None

class GraphJalan:
    def __init__(self):
        self.adj = {}
        self.persimpangan = {}

    def tambah_persimpangan(self, p):
        self.persimpangan[p.nama] = p
        self.adj[p.nama] = None

    def tambah_jalan(self, asal, tujuan, jarak, lajur, dua_arah=True):
        node = EdgeNode(tujuan, jarak, lajur)
        node.next = self.adj[asal]
        self.adj[asal] = node

        if dua_arah:
            node2 = EdgeNode(asal, jarak, lajur)
            node2.next = self.adj[tujuan]
            self.adj[tujuan] = node2

    def tetangga(self, nama):
        hasil = []
        curr = self.adj[nama]
        while curr:
            hasil.append((curr.dest, curr.jarak))
            curr = curr.next
        return hasil

# ================= BST =================
class BSTNode:
    def __init__(self, nama, p):
        self.nama = nama
        self.p = p
        self.left = self.right = None

class BSTJalan:
    def __init__(self):
        self.root = None

    def insert(self, nama, p):
        def _insert(root, nama, p):
            if not root:
                return BSTNode(nama, p)
            if nama < root.nama:
                root.left = _insert(root.left, nama, p)
            else:
                root.right = _insert(root.right, nama, p)
            return root
        self.root = _insert(self.root, nama, p)

    def search(self, nama):
        curr = self.root
        while curr:
            if nama == curr.nama:
                return curr.p
            elif nama < curr.nama:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def inorder(self):
        res = []
        def _in(root):
            if root:
                _in(root.left)
                res.append(root.nama)
                _in(root.right)
        _in(self.root)
        return res

# ================= DIJKSTRA =================
def dijkstra_rute(graph, asal):
    INF = float('inf')
    dist = {v: INF for v in graph.adj}
    parent = {v: None for v in graph.adj}
    visited = set()

    dist[asal] = 0

    while len(visited) < len(graph.adj):
        u = min((v for v in graph.adj if v not in visited), key=lambda x: dist[x])
        visited.add(u)

        curr = graph.adj[u]
        while curr:
            if dist[u] + curr.jarak < dist[curr.dest]:
                dist[curr.dest] = dist[u] + curr.jarak
                parent[curr.dest] = u
            curr = curr.next

    return dist, parent

# ================= GENERATOR =================
def generate_jaringan(n=25, seed=17):
    rng = np.random.default_rng(seed)
    nama_p = [f'P{i:02d}' for i in range(n)]
    persimpangan = [Persimpangan(nm, int(rng.integers(15, 30))) for nm in nama_p]

    perm = rng.permutation(n)
    edges = []

    for i in range(1, n):
        u = nama_p[perm[i-1]]
        v = nama_p[perm[i]]
        edges.append((u, v, int(rng.integers(100, 2000)), int(rng.integers(1, 4))))

    for _ in range(15):
        i, j = rng.choice(n, 2, replace=False)
        edges.append((nama_p[i], nama_p[j],
                      int(rng.integers(100,2000)),
                      int(rng.integers(1,4))))
    return persimpangan, edges

# ================= MAIN CLI =================
def main():
    graph = GraphJalan()
    bst_index = BSTJalan()
    queues = {}
    log_siklus = Stack()
    kendaraan_counter = 0

    persimpangan, edges = generate_jaringan(25, 17)

    for p in persimpangan:
        graph.tambah_persimpangan(p)
        bst_index.insert(p.nama, p)
        queues[p.nama] = PriorityQueueKendaraan()

    for u, v, j, l in edges:
        graph.tambah_jalan(u, v, j, l)

    print("Smart Traffic Simulation")
    print ("test")
    while True:
        cmd = input(">> ").split()

        if not cmd:
            continue

        if cmd[0] == "MASUK":
            nama, jenis = cmd[1], cmd[2]
            kendaraan_counter += 1

            k = Kendaraan(kendaraan_counter,
                          JENIS_KENDARAAN[jenis],
                          nama, "-", time.time())

            queues[nama].enqueue(k)
            print("Masuk antrian")

        elif cmd[0] == "BERANGKAT":
            nama = cmd[1]
            k = queues[nama].dequeue()
            print("Berangkat:", k)

        elif cmd[0] == "RUTE":
            asal, tujuan = cmd[1], cmd[2]
            dist, parent = dijkstra_rute(graph, asal)
            print("Jarak:", dist[tujuan])

        elif cmd[0] == "ANTRIAN":
            nama = cmd[1]
            print("Jumlah:", len(queues[nama]))

        elif cmd[0] == "KELUAR":
            print("TES")
            break

if __name__ == "__main__":
    main()
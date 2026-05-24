
import numpy as np
import random
import time
from dataclasses import dataclass

np.random.seed(17)
random.seed(17)

JENIS_KENDARAAN = {
    "AMBULANS": 1,
    "BUS": 2,
    "MOBIL": 3,
    "MOTOR": 4
}

NAMA_JENIS = {
    1: "AMBULANS",
    2: "BUS",
    3: "MOBIL",
    4: "MOTOR"
}

# ================= DATA =================

@dataclass
class Kendaraan:
    id_kendaraan: int
    jenis: int
    asal: str
    tujuan: str
    waktu_masuk: str

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

        if self.head is None:
            self.head = node

        elif kendaraan.jenis < self.head.data.jenis:
            node.next = self.head
            self.head = node

        else:
            curr = self.head

            while (curr.next and
                   curr.next.data.jenis <= kendaraan.jenis):
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

        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next
        self._size -= 1

        return data

    def peek(self):
        return self.top.data if self.top else None


# ================= GRAPH =================

class EdgeNode:

    def __init__(self, dest, jarak, lajur):
        self.dest = dest
        self.jarak = jarak
        self.lajur = lajur
        self.next = None


class GraphJalan:

    def __init__(self):
        self.adj = {}
        self.persimpangan = {}

    def tambah_persimpangan(self, p):
        self.persimpangan[p.nama] = p
        self.adj[p.nama] = None

    def tambah_jalan(self, asal, tujuan, jarak, lajur, dua_arah=True):

        n = EdgeNode(tujuan, jarak, lajur)
        n.next = self.adj[asal]
        self.adj[asal] = n

        if dua_arah:
            n2 = EdgeNode(asal, jarak, lajur)
            n2.next = self.adj[tujuan]
            self.adj[tujuan] = n2

    def tetangga(self, nama):

        hasil = []
        curr = self.adj[nama]

        while curr:
            hasil.append((curr.dest, curr.jarak))
            curr = curr.next

        return hasil

    def degree(self, nama):

        d = 0
        curr = self.adj[nama]

        while curr:
            d += 1
            curr = curr.next

        return d

    def dfs(self, start):

        visited = set()

        def _dfs(v):

            visited.add(v)

            curr = self.adj[v]

            while curr:
                if curr.dest not in visited:
                    _dfs(curr.dest)
                curr = curr.next

        _dfs(start)

        return visited


# ================= BST =================

class BSTNode:

    def __init__(self, nama, p):
        self.nama = nama
        self.p = p
        self.left = None
        self.right = None


class BSTJalan:

    def __init__(self):
        self.root = None

    def insert(self, nama, p):

        def _insert(root):

            if root is None:
                return BSTNode(nama, p)

            if nama < root.nama:
                root.left = _insert(root.left)
            else:
                root.right = _insert(root.right)

            return root

        self.root = _insert(self.root)

    def search(self, nama):

        curr = self.root

        while curr:

            if nama == curr.nama:
                return curr.p

            if nama < curr.nama:
                curr = curr.left
            else:
                curr = curr.right

        return None

    def inorder(self):

        hasil = []

        def _in(node):

            if node:
                _in(node.left)
                hasil.append(node.nama)
                _in(node.right)

        _in(self.root)

        return hasil


# ================= DIJKSTRA =================

def dijkstra_rute(graph, asal):

    INF = float("inf")

    dist = {v: INF for v in graph.adj}
    parent = {v: None for v in graph.adj}

    visited = set()
    dist[asal] = 0

    while len(visited) < len(graph.adj):

        u = min(
            (v for v in graph.adj if v not in visited),
            key=lambda x: dist[x]
        )

        visited.add(u)

        curr = graph.adj[u]

        while curr:

            if dist[u] + curr.jarak < dist[curr.dest]:
                dist[curr.dest] = dist[u] + curr.jarak
                parent[curr.dest] = u

            curr = curr.next

    return dist, parent


def ambil_jalur(parent, tujuan):

    path = []
    curr = tujuan

    while curr:
        path.append(curr)
        curr = parent[curr]

    path.reverse()

    return path


# ================= SORTING =================

def selection_sort(data):

    arr = data[:]

    n = len(arr)

    for i in range(n):

        idx = i

        for j in range(i + 1, n):

            if arr[j][1] > arr[idx][1]:
                idx = j

        arr[i], arr[idx] = arr[idx], arr[i]

    return arr


def insertion_sort(data):

    arr = data[:]

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j][1] < key[1]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# ================= UTIL =================

def generate_jaringan(n=100, seed=17):

    rng = np.random.default_rng(seed)

    nama_p = [f"P{i:02d}" for i in range(n)]

    persimpangan = [
        Persimpangan(nm, int(rng.integers(15, 30)))
        for nm in nama_p
    ]

    perm = rng.permutation(n)

    edges = []

    for i in range(1, n):

        u = nama_p[perm[i - 1]]
        v = nama_p[perm[i]]

        edges.append(
            (
                u,
                v,
                int(rng.integers(100, 2000)),
                int(rng.integers(1, 4))
            )
        )

    for _ in range(15):

        i, j = rng.choice(n, 2, replace=False)

        edges.append(
            (
                nama_p[i],
                nama_p[j],
                int(rng.integers(100, 2000)),
                int(rng.integers(1, 4))
            )
        )

    return persimpangan, edges


def tampil_bantuan():

    print("""
====================================================
BANTUAN

LIST_PERSIMPANGAN

MASUK <persimpangan> <jenis>
BERANGKAT <persimpangan>
ANTRIAN <persimpangan>

RUTE <asal> <tujuan>

INFO <persimpangan>

SIKLUS_LAMPU <persimpangan>
RIWAYAT_LAMPU

ISOLASI

LAPORAN_KEMACETAN_SELECTION
LAPORAN_KEMACETAN_INSERTION

KELUAR
====================================================
""")


# ================= MAIN =================

def main():

    graph = GraphJalan()
    bst = BSTJalan()
    log_siklus = Stack()

    queues = {}

    kendaraan_counter = 0

    persimpangan, edges = generate_jaringan(100, 17)

    for p in persimpangan:

        graph.tambah_persimpangan(p)
        bst.insert(p.nama, p)

        queues[p.nama] = PriorityQueueKendaraan()

    for u, v, j, l in edges:
        graph.tambah_jalan(u, v, j, l)

    print("SMART TRAFFIC SIMULATION")
    print("Ketik BANTUAN")

    while True:

        try:
            cmd = input(">> ").strip().split()

            if not cmd:
                continue

            aksi = cmd[0].upper()

            if aksi == "BANTUAN":
                tampil_bantuan()

            elif aksi == "LIST_PERSIMPANGAN":
                print(bst.inorder())
                print("Big-O = O(n)")

            elif aksi == "MASUK":

                nama = cmd[1].upper()
                jenis = cmd[2].upper()

                kendaraan_counter += 1

                k = Kendaraan(
                    kendaraan_counter,
                    JENIS_KENDARAAN[jenis],
                    nama,
                    "-",
                    time.strftime("%d-%m-%Y %I:%M:%S %p")
                )
                queues[nama].enqueue(k)

                print("Kendaraan masuk")
                print("Big-O = O(n)")

            elif aksi == "BERANGKAT":

                nama = cmd[1].upper()

                k = queues[nama].dequeue()

                if k:

                    print("\n===================================")
                    print("      KENDARAAN BERANGKAT")
                    print("===================================")
                    print(f"ID Kendaraan : {k.id_kendaraan}")
                    print(f"Jenis        : {NAMA_JENIS[k.jenis]}")
                    print(f"Asal         : {k.asal}")
                    print(f"Waktu Masuk  : {k.waktu_masuk}")
                    print("===================================")

                else:
                    print("Antrian kosong")

                print("Big-O = O(1)")

            elif aksi == "ANTRIAN":

                nama = cmd[1].upper()

                print("Jumlah:", len(queues[nama]))
                print("Big-O = O(1)")

            elif aksi == "INFO":

                nama = cmd[1].upper()

                p = bst.search(nama)

                if p:
                    print("Nama:", p.nama)
                    print("Kapasitas:", p.kapasitas)

                print("Big-O rata-rata = O(log n)")

            elif aksi == "RUTE":

                asal = cmd[1].upper()
                tujuan = cmd[2].upper()

                dist, parent = dijkstra_rute(graph, asal)

                path = ambil_jalur(parent, tujuan)

                print("Rute :", " -> ".join(path))
                print("Jarak:", dist[tujuan], "meter")
                print("Big-O = O(V^2 + E)")

            elif aksi == "SIKLUS_LAMPU":

                p = cmd[1].upper()

                kondisi = random.choice(
                    ["HIJAU", "KUNING", "MERAH"]
                )

                log_siklus.push(
                    (p, kondisi, time.ctime())
                )

                print(f"{p} => {kondisi}")
                print("Big-O = O(1)")

            elif aksi == "RIWAYAT_LAMPU":

                data = log_siklus.peek()

                if data:
                    print(data)
                else:
                    print("Belum ada riwayat")

                print("Big-O = O(1)")

            elif aksi == "ISOLASI":

                start = next(iter(graph.adj))

                visited = graph.dfs(start)

                isolasi = [
                    v for v in graph.adj
                    if v not in visited
                ]

                print("Terisolasi:", isolasi)
                print("Big-O = O(V+E)")

            elif aksi == "LAPORAN_KEMACETAN_SELECTION":

                data = [
                    (p, len(queues[p]))
                    for p in queues
                ]

                hasil = selection_sort(data)

                for p, j in hasil:
                    print(f"{p}: {j}")

                print("Big-O = O(n^2)")

            elif aksi == "LAPORAN_KEMACETAN_INSERTION":

                data = [
                    (p, len(queues[p]))
                    for p in queues
                ]

                hasil = insertion_sort(data)

                for p, j in hasil:
                    print(f"{p}: {j}")

                print("Big-O = O(n^2)")

            elif aksi == "KELUAR":

                print("Program selesai")
                break

            else:
                print("Perintah tidak dikenal")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

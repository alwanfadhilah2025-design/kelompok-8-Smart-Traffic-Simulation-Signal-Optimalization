import time
import random
from modul_graph_network import GraphJalan, generate_jaringan
from modul_priority_queue import PriorityQueueKendaraan, Kendaraan
from modul_dijkstra import dijkstra_rute
from modul_bst_index import BSTJalan
from modul_sorting import selection_sort_by_queue_length


class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    def __init__(self):
        self.top = None
    def push(self, data):
        node = self.Node(data)
        node.next = self.top
        self.top = node
    def pop(self):
        if not self.top:
            return None
        val = self.top.data
        self.top = self.top.next
        return val

ARAH = ['UTARA', 'SELATAN', 'TIMUR', 'BARAT']
JENIS_KENDARAAN = {'AMBULANS': 1, 'BUS': 2, 'MOBIL': 3, 'MOTOR': 4}

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
        graph.tambah_jalan(u, v, j, l, dua_arah=True)

    print("Smart Traffic Simulation - Topik 7")
    print("Perintah: MASUK, BERANGKAT, RUTE, ANTRIAN, SIKLUS_LAMPU, LAPORAN_KEMACETAN, ISOLASI, GENERATE, KELUAR")

    while True:
        cmd = input(">> ").strip().split()
        if not cmd:
            continue

        if cmd[0].upper() == "MASUK":
            if len(cmd) != 3:
                print("Format: MASUK <persimpangan> <jenis>")
                continue
            nama, jenis = cmd[1], cmd[2].upper()
            if jenis not in JENIS_KENDARAAN:
                print("Jenis harus AMBULANS/BUS/MOBIL/MOTOR")
                continue
            if nama not in queues:
                print("Persimpangan tidak ditemukan")
                continue
            kendaraan_counter += 1
            k = Kendaraan(kendaraan_counter, JENIS_KENDARAAN[jenis], nama, "-", time.time())
            queues[nama].enqueue(k)
            print(f"Kendaraan {jenis} masuk antrian {nama} | Big-O: O(n)")

        elif cmd[0].upper() == "BERANGKAT":
            if len(cmd) != 2:
                print("Format: BERANGKAT <persimpangan>")
                continue
            nama = cmd[1]
            if nama not in queues:
                print("Persimpangan tidak ditemukan")
                continue
            k = queues[nama].dequeue()
            if k:
                jenis = [j for j, val in JENIS_KENDARAAN.items() if val == k.jenis][0]
                print(f"{jenis} ID={k.id_kendaraan} berangkat dari {nama} | Big-O: O(1)")
            else:
                print(f"Antrian {nama} kosong")

        elif cmd[0].upper() == "RUTE":
            if len(cmd) != 3:
                print("Format: RUTE <asal> <tujuan>")
                continue
            asal, tujuan = cmd[1], cmd[2]
            if asal not in graph.adj or tujuan not in graph.adj:
                print("Persimpangan tidak valid")
                continue
            dist, _ = dijkstra_rute(graph, asal)
            if dist[tujuan] == float('inf'):
                print(f"Tidak ada rute dari {asal} ke {tujuan}")
            else:
                print(f"Jarak terpendek {asal} -> {tujuan} = {dist[tujuan]} meter | Big-O: O(V^2)")

        elif cmd[0].upper() == "ANTRIAN":
            if len(cmd) != 2:
                print("Format: ANTRIAN <persimpangan>")
                continue
            nama = cmd[1]
            if nama not in queues:
                print("Persimpangan tidak ditemukan")
                continue
            print(f"Antrian di {nama}: {len(queues[nama])} kendaraan | Big-O: O(1)")

        elif cmd[0].upper() == "SIKLUS_LAMPU":
            if len(cmd) != 2:
                print("Format: SIKLUS_LAMPU <persimpangan>")
                continue
            p = cmd[1]
            if p not in queues:
                print("Persimpangan tidak ditemukan")
                continue
            arah = ARAH[len(queues[p]) % 4]
            log_siklus.push((p, arah, time.time()))
            print(f"Lampu {p} => {arah} | Big-O: O(1)")

        elif cmd[0].upper() == "LAPORAN_KEMACETAN":
            data = []
            for nama in queues:
                jml = len(queues[nama])
                kap = graph.persimpangan[nama].kapasitas
                data.append((nama, jml, kap))
            
            sorted_data = selection_sort_by_queue_length([(d[0], d[1]) for d in data])
            print("\n=== LAPORAN KEMACETAN (Terurut antrian terkecil ke terbesar) ===")
            print(f"{'Persimpangan':<12} {'Antrian':<8} {'Kapasitas':<10} {'Status':<8}")
            for nama, jml in sorted_data:
                kap = graph.persimpangan[nama].kapasitas
                status = "MACET" if jml > kap else "LANCAR"
                print(f"{nama:<12} {jml:<8} {kap:<10} {status:<8}")
            print("Metode sorting: Selection Sort | Big-O: O(n^2)\n")

        elif cmd[0].upper() == "ISOLASI":
            
            if not graph.adj:
                print("Tidak ada persimpangan")
                continue
            start = next(iter(graph.adj))
            visited = set()
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for tetangga, _ in graph.tetangga(node):
                        if tetangga not in visited:
                            stack.append(tetangga)
            semua = set(graph.adj.keys())
            terisolasi = semua - visited
            if not terisolasi:
                print("Semua persimpangan terhubung dengan baik.")
            else:
                print(f"Persimpangan terisolasi: {', '.join(sorted(terisolasi))}")
            print("| Deteksi menggunakan DFS | Big-O: O(V+E)")

        elif cmd[0].upper() == "GENERATE":
            if len(cmd) != 2:
                print("Format: GENERATE <jumlah>")
                continue
            try:
                jumlah = int(cmd[1])
            except:
                print("Jumlah harus angka")
                continue
            for _ in range(jumlah):
                nama_persimpangan = random.choice(list(queues.keys()))
                jenis_kendaraan = random.choice(list(JENIS_KENDARAAN.keys()))
                kendaraan_counter += 1
                k = Kendaraan(kendaraan_counter, JENIS_KENDARAAN[jenis_kendaraan],
                              nama_persimpangan, "-", time.time())
                queues[nama_persimpangan].enqueue(k)
            print(f"{jumlah} kendaraan ditambahkan ke antrian acak | Big-O: O(jumlah * n)")

        elif cmd[0].upper() == "KELUAR":
            print("Simulasi selesai.")
            break

        else:
            print("Perintah tidak dikenal. Gunakan: MASUK, BERANGKAT, RUTE, ANTRIAN, SIKLUS_LAMPU, LAPORAN_KEMACETAN, ISOLASI, GENERATE, KELUAR")

if __name__ == "__main__":
    main()

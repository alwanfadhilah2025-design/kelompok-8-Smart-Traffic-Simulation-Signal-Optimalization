from modules.modul1_graph import cek_isolasi
from data_structures.graph import GraphJalan

class P:
    def __init__(self, nama):
        self.nama = nama

g = GraphJalan()

g.tambah_persimpangan(P("P01"))
g.tambah_persimpangan(P("P02"))
g.tambah_persimpangan(P("P03"))

g.tambah_jalan("P01", "P02", 100, 2)

isolasi = cek_isolasi(g)

print("Hasil isolasi:", isolasi)

assert "P03" in isolasi

print("TEST MODUL GRAPH BERHASIL")

from modules.modul3_dijkstra import (
    dijkstra_rute,
    ambil_jalur
)

from data_structures.graph import GraphJalan

class P:

    def __init__(self, nama):
        self.nama = nama

g = GraphJalan()

g.tambah_persimpangan(P("P01"))
g.tambah_persimpangan(P("P02"))
g.tambah_persimpangan(P("P03"))

g.tambah_jalan("P01","P02",100,2)
g.tambah_jalan("P02","P03",150,2)

dist,parent = dijkstra_rute(g,"P01")

path = ambil_jalur(parent,"P03")

print("Rute :", path)
print("Jarak:", dist["P03"])

assert dist["P03"] == 250

print("TEST DIJKSTRA BERHASIL")

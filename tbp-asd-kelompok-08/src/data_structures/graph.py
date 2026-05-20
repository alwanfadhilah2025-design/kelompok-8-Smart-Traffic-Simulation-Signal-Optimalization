class EdgeNode:
    def __init__(self, dest, jarak, kapasitas_lajur):
        self.dest = dest
        self.jarak = jarak
        self.kapasitas_lajur = kapasitas_lajur
        self.next = None

class GraphJalan:
    def __init__(self):
        self.adj = {}          # adjacency list: node_name -> EdgeNode (linked list)
        self.persimpangan = {} # menyimpan objek Persimpangan

    def tambah_persimpangan(self, p):
        self.persimpangan[p.nama] = p
        self.adj[p.nama] = None

    def tambah_jalan(self, asal, tujuan, jarak, lajur, dua_arah=True):
        """O(1) tambah edge dari asal ke tujuan"""
        node = EdgeNode(tujuan, jarak, lajur)
        node.next = self.adj[asal]
        self.adj[asal] = node

        if dua_arah:
            node2 = EdgeNode(asal, jarak, lajur)
            node2.next = self.adj[tujuan]
            self.adj[tujuan] = node2

    def tetangga(self, nama):
        """O(deg) mengembalikan list (dest, jarak)"""
        hasil = []
        curr = self.adj[nama]
        while curr:
            hasil.append((curr.dest, curr.jarak))
            curr = curr.next
        return hasil

    def degree(self, nama):
        """Jumlah edge keluar dari simpul nama"""
        count = 0
        curr = self.adj[nama]
        while curr:
            count += 1
            curr = curr.next
        return count

    def semua_simpul(self):
        return list(self.adj.keys())

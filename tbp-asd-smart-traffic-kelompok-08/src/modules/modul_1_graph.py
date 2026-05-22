@dataclass
class Persimpangan:
    nama: str
    kapasitas: int = 20

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

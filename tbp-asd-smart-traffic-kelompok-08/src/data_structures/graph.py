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

    def tambah_jalan(
        self,
        asal,
        tujuan,
        jarak,
        lajur,
        dua_arah=True
    ):

        node = EdgeNode(
            tujuan,
            jarak,
            lajur
        )

        node.next = self.adj[asal]
        self.adj[asal] = node

        if dua_arah:

            node2 = EdgeNode(
                asal,
                jarak,
                lajur
            )

            node2.next = self.adj[tujuan]
            self.adj[tujuan] = node2

    def tetangga(self, nama):

        hasil = []

        curr = self.adj[nama]

        while curr:
            hasil.append(
                (curr.dest, curr.jarak)
            )
            curr = curr.next

        return hasil

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

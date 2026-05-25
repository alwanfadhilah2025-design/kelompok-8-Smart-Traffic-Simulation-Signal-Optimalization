from data_structures.bst import BSTJalan

class P:

    def __init__(self,nama):
        self.nama = nama

bst = BSTJalan()

bst.insert("P03",P("P03"))
bst.insert("P01",P("P01"))
bst.insert("P02",P("P02"))

hasil = bst.search("P02")

print("Ditemukan:",hasil.nama)

assert hasil.nama == "P02"

print("TEST BST BERHASIL")

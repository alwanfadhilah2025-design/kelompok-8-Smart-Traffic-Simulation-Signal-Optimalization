class BSTNode:
    def __init__(self, nama, p):
        self.nama = nama   # key (nama persimpangan)
        self.p = p         # data (objek Persimpangan)
        self.left = None
        self.right = None

class BSTJalan:
    def __init__(self):
        self.root = None

    def insert(self, nama, p):
        """O(log n) rata-rata, O(n) worst-case"""
        def _insert(root, nama, p):
            if root is None:
                return BSTNode(nama, p)
            if nama < root.nama:
                root.left = _insert(root.left, nama, p)
            else:
                root.right = _insert(root.right, nama, p)
            return root
        self.root = _insert(self.root, nama, p)

    def search(self, nama):
        """O(log n) rata-rata"""
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
        """Mengembalikan daftar nama persimpangan terurut"""
        res = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                res.append(node.nama)
                _inorder(node.right)
        _inorder(self.root)
        return res

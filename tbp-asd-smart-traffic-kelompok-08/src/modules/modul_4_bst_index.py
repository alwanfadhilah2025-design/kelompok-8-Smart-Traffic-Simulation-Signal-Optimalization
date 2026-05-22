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

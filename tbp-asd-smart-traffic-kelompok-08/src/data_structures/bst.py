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

            if curr.nama == nama:
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

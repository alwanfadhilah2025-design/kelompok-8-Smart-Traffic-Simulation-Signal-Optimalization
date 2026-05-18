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
 


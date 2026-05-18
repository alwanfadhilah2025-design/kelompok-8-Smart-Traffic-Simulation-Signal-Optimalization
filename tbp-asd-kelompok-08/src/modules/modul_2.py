class PriorityQueueKendaraan:
      def __init__(self):
          self.head = None
          self._size = 0
   
      def enqueue(self, kendaraan):
          node = LLNode(kendaraan)
   
          if not self.head or kendaraan.jenis < self.head.data.jenis:
             node.next = self.head
             self.head = node
         else:             curr = self.head
             while curr.next and curr.next.data.jenis <= kendaraan.jenis:
                 curr = curr.next
             node.next = curr.next
             curr.next = node
  
         self._size += 1
  
     def dequeue(self):
         if not self.head:
             return None
         val = self.head.data
         self.head = self.head.next
         self._size -= 1
         return val
  
     def __len__(self):
         return self._size
  
 class Stack:
     def __init__(self):
         self.top = None
         self._size = 0
  
     def push(self, data):
         node = LLNode(data)
         node.next = self.top
         self.top = node
         self._size += 1
  
     def pop(self):
         if not self.top:
             return None
         val = self.top.data
         self.top = self.top.next
         self._size -= 1
         return val
  
     def peek(self):
         return self.top.data if self.top else None
 


 import numpy as np, time, random
  from dataclasses import dataclass
  from typing import Optional, List, Dict, Tuple
   
  np.random.seed(17)
  random.seed(17)
   
  ARAH = ['UTARA', 'SELATAN', 'TIMUR', 'BARAT']
  JENIS_KENDARAAN = {'AMBULANS': 1, 'BUS': 2, 'MOBIL': 3, 'MOTOR': 4}
 @dataclass
 class Kendaraan:
  id_kendaraan: int
     jenis: int
     asal: str
     tujuan: str
     waktu_masuk: float
  
 @dataclass
 class Persimpangan:
    nama: str
     kapasitas: int = 100
 class LLNode:
     def __init__(self, data=None):
         self.data = data
         self.next = None



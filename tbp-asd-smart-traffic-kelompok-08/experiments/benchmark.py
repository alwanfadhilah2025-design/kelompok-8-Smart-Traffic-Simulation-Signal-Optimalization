
N = 10
PS C:\Users\VICTUS\OneDrive\Documents\Project VS code Semester 2> python -u "c:\Users\VICTUS\OneDrive\Documents\Project VS code Semester 2\main.py"
SMART TRAFFIC SIMULATION
Ketik BANTUAN
>> BANTUAN

====================================================
BANTUAN

LIST_PERSIMPANGAN

MASUK <persimpangan> <jenis>
BERANGKAT <persimpangan>
ANTRIAN <persimpangan>

RUTE <asal> <tujuan>

INFO <persimpangan>

SIKLUS_LAMPU <persimpangan>
RIWAYAT_LAMPU

ISOLASI

LAPORAN_KEMACETAN_SELECTION
LAPORAN_KEMACETAN_INSERTION

KELUAR
====================================================

>> LIST_PERSIMPANGAN
['P00', 'P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09']
Big-O = O(n)
>> MASUK P01 MOBIL
Kendaraan masuk
Big-O = O(n)
>> MASUK P02 MOTOR
Kendaraan masuk
Big-O = O(n)
>> MASUK P01 MOBIL
Kendaraan masuk
Big-O = O(n)
>> MASUK P01 AMBULANS
Kendaraan masuk
Big-O = O(n)
>> MASUK P01 BUS
Kendaraan masuk
Big-O = O(n)
>> ANTRIAN P01
Jumlah: 4
Big-O = O(1)
>> BERANGKAT P01

===================================
      KENDARAAN BERANGKAT
===================================
ID Kendaraan : 4
Jenis        : AMBULANS
Asal         : P01
Waktu Masuk  : 24-05-2026 08:28:22 PM
===================================
Big-O = O(1)
>> INFO P01
Nama: P01
Kapasitas: 27
Big-O rata-rata = O(log n)
>> RUTE P01 P06
Rute : P01 -> P02 -> P06
Jarak: 1723 meter
Big-O = O(V^2 + E)
>> SIKLUS_LAMPU P01
P01 => MERAH
Big-O = O(1)
>> RIWAYAT_LAMPU
('P01', 'MERAH', 'Sun May 24 20:30:16 2026')
Big-O = O(1)
>> ISOLASI
Terisolasi: []
Big-O = O(V+E)
>> LAPORAN_KEMACETAN_SELECTION
P01: 3
P02: 1
P00: 0
P03: 0
P04: 0
P05: 0
P06: 0
P07: 0
P08: 0
P09: 0
Big-O = O(n^2)
>> LAPORAN_KEMACETAN_INSERTION
P01: 3
P02: 1
P00: 0
P03: 0
P04: 0
P05: 0
P06: 0
P07: 0
P08: 0
P09: 0
Big-O = O(n^2)
>> KELUAR
Program selesai


N = 25
PS C:\Users\VICTUS\OneDrive\Documents\Project VS code Semester 2> python -u "c:\Users\VICTUS\OneDrive\Documents\Project VS code Semester 2\main.py"
SMART TRAFFIC SIMULATION
Ketik BANTUAN
>> BANTUAN

====================================================
BANTUAN

LIST_PERSIMPANGAN

MASUK <persimpangan> <jenis>
BERANGKAT <persimpangan>
ANTRIAN <persimpangan>

RUTE <asal> <tujuan>

INFO <persimpangan>

SIKLUS_LAMPU <persimpangan>
RIWAYAT_LAMPU

ISOLASI

LAPORAN_KEMACETAN_SELECTION
LAPORAN_KEMACETAN_INSERTION

KELUAR
====================================================

>> LIST_PERSIMPANGAN
['P00', 'P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24']
Big-O = O(n)
>> MASUK P03 MOTOR
Kendaraan masuk
Big-O = O(n)
>> MASUK P03 MOBIL
Kendaraan masuk
Big-O = O(n)
>> MASUK P03 BUS
Kendaraan masuk
Big-O = O(n)
>> MASUK P03 MOTOR
Kendaraan masuk
Big-O = O(n)
>> MASUK P02 MOBIL
Kendaraan masuk
Big-O = O(n)
>> ANTRIAN P03
Jumlah: 4
Big-O = O(1)
>> BERANGKAT P03

===================================
      KENDARAAN BERANGKAT
===================================
ID Kendaraan : 3
Jenis        : BUS
Asal         : P03
Waktu Masuk  : 24-05-2026 08:44:39 PM
===================================
Big-O = O(1)
>> INFO P03
Nama: P03
Kapasitas: 17
Big-O rata-rata = O(log n)
>> RUTE P03 P20
Rute : P03 -> P22 -> P00 -> P20
Jarak: 1866 meter
Big-O = O(V^2 + E)
>> SIKLUS_LAMPU P03
P03 => MERAH
Big-O = O(1)
>> RIWAYAT_LAMPU
('P03', 'MERAH', 'Sun May 24 20:46:15 2026')
Big-O = O(1)
>> ISOLASI
Terisolasi: []
Big-O = O(V+E)
>> LAPORAN_KEMACETAN_SELECTION
P03: 3
P02: 1
P01: 0
P00: 0
P04: 0
P05: 0
P06: 0
P07: 0
P08: 0
P09: 0
P10: 0
P11: 0
P12: 0
P13: 0
P14: 0
P15: 0
P16: 0
P17: 0
P18: 0
P19: 0
P20: 0
P21: 0
P22: 0
P23: 0
P24: 0
Big-O = O(n^2)
>> LAPORAN_KEMACETAN_INSERTION
P03: 3
P02: 1
P00: 0
P01: 0
P04: 0
P05: 0
P06: 0
P07: 0
P08: 0
P09: 0
P10: 0
P11: 0
P12: 0
P13: 0
P14: 0
P15: 0
P16: 0
P17: 0
P18: 0
P19: 0
P20: 0
P21: 0
P22: 0
P23: 0
P24: 0
Big-O = O(n^2)
>> KELUAR


N = 100
Program selesai
PS C:\Users\VICTUS\OneDrive\Documents\Project VS code Semester 2> python -u "c:\Users\VICTUS\OneDrive\Documents\Project VS code Semester 2\main.py"
SMART TRAFFIC SIMULATION
Ketik BANTUAN
>> BANTUAN

====================================================
BANTUAN

LIST_PERSIMPANGAN

MASUK <persimpangan> <jenis>
BERANGKAT <persimpangan>
ANTRIAN <persimpangan>

RUTE <asal> <tujuan>

INFO <persimpangan>

SIKLUS_LAMPU <persimpangan>
RIWAYAT_LAMPU

ISOLASI

LAPORAN_KEMACETAN_SELECTION
LAPORAN_KEMACETAN_INSERTION

KELUAR
====================================================

>> LIST_PERSIMPANGAN
['P00', 'P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25', 'P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33', 'P34', 'P35', 'P36', 'P37', 'P38', 'P39', 'P40', 'P41', 'P42', 'P43', 'P44', 'P45', 'P46', 'P47', 'P48', 'P49', 'P50', 'P51', 'P52', 'P53', 'P54', 'P55', 'P56', 'P57', 'P58', 'P59', 'P60', 'P61', 'P62', 'P63', 'P64', 'P65', 'P66', 'P67', 'P68', 'P69', 'P70', 'P71', 'P72', 'P73', 'P74', 'P75', 'P76', 'P77', 'P78', 'P79', 'P80', 'P81', 'P82', 'P83', 'P84', 'P85', 'P86', 'P87', 'P88', 'P89', 'P90', 'P91', 'P92', 'P93', 'P94', 'P95', 'P96', 'P97', 'P98', 'P99']
Big-O = O(n)
>> MASUK P10 AMBULANS
Kendaraan masuk
Big-O = O(n)
>> MASUK P10 MOBIL
Kendaraan masuk
Big-O = O(n)
>> MASUK P10 MOBIL
Kendaraan masuk
Big-O = O(n)
>> MASUK P10 MOTOR
Kendaraan masuk
Big-O = O(n)
>> MASUK P10 MOTOR
Kendaraan masuk
Big-O = O(n)
>> MASUK P10 BUS
Kendaraan masuk
Big-O = O(n)
>> MASUK P10 BUS
Kendaraan masuk
Big-O = O(n)
>> ANTRIAN P10
Jumlah: 7
Big-O = O(1)
>> BERANGKAT P10

===================================
      KENDARAAN BERANGKAT
===================================
ID Kendaraan : 1
Jenis        : AMBULANS
Asal         : P10
Waktu Masuk  : 24-05-2026 08:54:37 PM
===================================
Big-O = O(1)
>> INFO P10 
Nama: P10
Kapasitas: 21
Big-O rata-rata = O(log n)
>> RUTE P10 P50
Rute : P10 -> P02 -> P29 -> P06 -> P93 -> P17 -> P41 -> P81 -> P88 -> P72 -> P71 -> P50
Jarak: 13259 meter
Big-O = O(V^2 + E)
>> SIKLUS_LAMPU P10
P10 => MERAH
Big-O = O(1)
>> RIWAYAT_LAMPU
('P10', 'MERAH', 'Sun May 24 20:58:16 2026')
Big-O = O(1)
>> ISOLASI
Terisolasi: []
Big-O = O(V+E)
>> LAPORAN_KEMACETAN_SELECTION
P10: 6
P01: 0
P02: 0
P03: 0
P04: 0
P05: 0
P06: 0
P07: 0
P08: 0
P09: 0
P00: 0
P11: 0
P12: 0
P13: 0
P14: 0
P15: 0
P16: 0
P17: 0
P18: 0
P19: 0
P20: 0
P21: 0
P22: 0
P23: 0
P24: 0
P25: 0
P26: 0
P27: 0
P28: 0
P29: 0
P30: 0
P31: 0
P32: 0
P33: 0
P34: 0
P35: 0
P36: 0
P37: 0
P38: 0
P39: 0
P40: 0
P41: 0
P42: 0
P43: 0
P44: 0
P45: 0
P46: 0
P47: 0
P48: 0
P49: 0
P50: 0
P51: 0
P52: 0
P53: 0
P54: 0
P55: 0
P56: 0
P57: 0
P58: 0
P59: 0
P60: 0
P61: 0
P62: 0
P63: 0
P64: 0
P65: 0
P66: 0
P67: 0
P68: 0
P69: 0
P70: 0
P71: 0
P72: 0
P73: 0
P74: 0
P75: 0
P76: 0
P77: 0
P78: 0
P79: 0
P80: 0
P81: 0
P82: 0
P83: 0
P84: 0
P85: 0
P86: 0
P87: 0
P88: 0
P89: 0
P90: 0
P91: 0
P92: 0
P93: 0
P94: 0
P95: 0
P96: 0
P97: 0
P98: 0
P99: 0
Big-O = O(n^2)
>> LAPORAN_KEMACETAN_INSERTION
P10: 6
P00: 0
P01: 0
P02: 0
P03: 0
P04: 0
P05: 0
P06: 0
P07: 0
P08: 0
P09: 0
P11: 0
P12: 0
P13: 0
P14: 0
P15: 0
P16: 0
P17: 0
P18: 0
P19: 0
P20: 0
P21: 0
P22: 0
P23: 0
P24: 0
P25: 0
P26: 0
P27: 0
P28: 0
P29: 0
P30: 0
P31: 0
P32: 0
P33: 0
P34: 0
P35: 0
P36: 0
P37: 0
P38: 0
P39: 0
P40: 0
P41: 0
P42: 0
P43: 0
P44: 0
P45: 0
P46: 0
P47: 0
P48: 0
P49: 0
P50: 0
P51: 0
P52: 0
P53: 0
P54: 0
P55: 0
P56: 0
P57: 0
P58: 0
P59: 0
P60: 0
P61: 0
P62: 0
P63: 0
P64: 0
P65: 0
P66: 0
P67: 0
P68: 0
P69: 0
P70: 0
P71: 0
P72: 0
P73: 0
P74: 0
P75: 0
P76: 0
P77: 0
P78: 0
P79: 0
P80: 0
P81: 0
P82: 0
P83: 0
P84: 0
P85: 0
P86: 0
P87: 0
P88: 0
P89: 0
P90: 0
P91: 0
P92: 0
P93: 0
P94: 0
P95: 0
P96: 0
P97: 0
P98: 0
P99: 0
Big-O = O(n^2)
>> KELUAR
Program selesai
PS C:\Users\VICTUS\OneDrive\Documents\Project VS code Semester 2> 

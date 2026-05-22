N = 10

PS C:\Users\ASUS\OneDrive\ドキュメント\arwan codingan> python -u "c:\Users\ASUS\OneDrive\ドキュメント\arwan codingan\wan"
Smart Traffic Simulation
>> MASUK P01 AMBULANS
Masuk antrian | Big-O: O(n)
>> MASUK P01 MOTOR
Masuk antrian | Big-O: O(n)
>> MASUK P03 MOBIL
Masuk antrian | Big-O: O(n)
>> MASUK P06 MOTOR
Masuk antrian | Big-O: O(n)
>> ANTRIAN P01
Jumlah: 2 | Big-O: O(1)
>> BERANGKAT P01 AMBULANS
Berangkat: Kendaraan(id_kendaraan=1, jenis=1, asal='P01', tujuan='-', waktu_masuk=1779337520.8409078) | Big-O: O(1)
>> RUTE P01 P09
Jarak: 1788 | Big-O: O(V^2)
>> SIKLUS_LAMPU P01
Siklus P01: SELATAN | Big-O: O(1)
>> LAPORAN_KEMACETAN
P00: LANCAR (0/26)
P01: LANCAR (1/27)
P02: LANCAR (0/16)
P03: LANCAR (1/17)
P04: LANCAR (0/21)
P05: LANCAR (0/23)
P06: LANCAR (1/26)
P07: LANCAR (0/20)
P08: LANCAR (0/15)
P09: LANCAR (0/18)
Big-O: O(n)
>> ISOLASI
Rollback: ('P01', 'SELATAN', 1779337613.1007829) | Big-O: O(1)
>> KELUAR
PS C:\Users\ASUS\OneDrive\ドキュメント\arwan codingan> 


N = 25

PS C:\Users\ASUS\OneDrive\ドキュメント\arwan codingan> python -u "c:\Users\ASUS\OneDrive\ドキュメント\arwan codingan\wan"
Smart Traffic Simulation
>> MASUK P02 MOTOR
Masuk antrian | Big-O: O(n)
>> MASUK P04 MOBIL
Masuk antrian | Big-O: O(n)
>> MASUK P04 BUS
Masuk antrian | Big-O: O(n)
>> MASUK P04 MOTOR
Masuk antrian | Big-O: O(n)
>> MASUK P09 BUS
Masuk antrian | Big-O: O(n)
>> MASUK P01 AMBULANS
Masuk antrian | Big-O: O(n)
>> ANTRIAN P04
Jumlah: 3 | Big-O: O(1)
>> BERANGKAT P04 MOBIL
Berangkat: Kendaraan(id_kendaraan=3, jenis=2, asal='P04', tujuan='-', waktu_masuk=1779337691.7046504) | Big-O: O(1)
>> RUTE P04 P23
Jarak: 1738 | Big-O: O(V^2)
>> SIKLUS_LAMPU P04
Siklus P04: TIMUR | Big-O: O(1)
>> LAPORAN_KEMACETAN
P00: LANCAR (0/26)
P01: LANCAR (1/27)
P02: LANCAR (1/16)
P03: LANCAR (0/17)
P04: LANCAR (2/21)
P05: LANCAR (0/23)
P06: LANCAR (0/26)
P07: LANCAR (0/20)
P08: LANCAR (0/15)
P09: LANCAR (1/18)
P10: LANCAR (0/21)
P11: LANCAR (0/20)
P12: LANCAR (0/28)
P13: LANCAR (0/21)
P14: LANCAR (0/24)
P15: LANCAR (0/24)
P16: LANCAR (0/16)
P17: LANCAR (0/26)
P18: LANCAR (0/15)
P19: LANCAR (0/15)
P20: LANCAR (0/23)
P21: LANCAR (0/18)
P22: LANCAR (0/20)
P23: LANCAR (0/24)
P24: LANCAR (0/17)
Big-O: O(n)
>> ISOLASI
Rollback: ('P04', 'TIMUR', 1779337801.5860605) | Big-O: O(1)
>> KELUAR


N = 100

PS C:\Users\ASUS\OneDrive\ドキュメント\arwan codingan> python -u "c:\Users\ASUS\OneDrive\ドキュメント\arwan codingan\wan"
Smart Traffic Simulation
>> MASUK P10 AMBULANS
Masuk antrian | Big-O: O(n)
>> MASUK P01 MOTOR
Masuk antrian | Big-O: O(n)
>> MASUK P11 MOBIL
Masuk antrian | Big-O: O(n)
>> MASUK P11 BUS
Masuk antrian | Big-O: O(n)
>> MASUK P11 AMBULANS
Masuk antrian | Big-O: O(n)
>> MASUK P09 MOTOR
Masuk antrian | Big-O: O(n)
>> ANTRIAN P11
Jumlah: 3 | Big-O: O(1)
>> BERANGKAT P11 BUS
Berangkat: Kendaraan(id_kendaraan=5, jenis=1, asal='P11', tujuan='-', waktu_masuk=1779338043.8161001) | Big-O: O(1)
>> RUTE P11 P50
Jarak: 13517 | Big-O: O(V^2)
>> SIKLUS_LAMPU P11
Siklus P11: TIMUR | Big-O: O(1)
>> LAPORAN_KEMACETAN
P00: LANCAR (0/26)
P01: LANCAR (1/27)
P02: LANCAR (0/16)
P03: LANCAR (0/17)
P04: LANCAR (0/21)
P05: LANCAR (0/23)
P06: LANCAR (0/26)
P07: LANCAR (0/20)
P08: LANCAR (0/15)
P09: LANCAR (1/18)
P10: LANCAR (1/21)
P11: LANCAR (2/20)
P12: LANCAR (0/28)
P13: LANCAR (0/21)
P14: LANCAR (0/24)
P15: LANCAR (0/24)
P16: LANCAR (0/16)
P17: LANCAR (0/26)
P18: LANCAR (0/15)
P19: LANCAR (0/15)
P20: LANCAR (0/23)
P21: LANCAR (0/18)
P22: LANCAR (0/20)
P23: LANCAR (0/24)
P24: LANCAR (0/17)
P25: LANCAR (0/16)
P26: LANCAR (0/25)
P27: LANCAR (0/29)
P28: LANCAR (0/25)
P29: LANCAR (0/27)
P30: LANCAR (0/21)
P31: LANCAR (0/15)
P32: LANCAR (0/24)
P33: LANCAR (0/23)
P34: LANCAR (0/26)
P35: LANCAR (0/24)
P36: LANCAR (0/22)
P37: LANCAR (0/15)
P38: LANCAR (0/25)
P39: LANCAR (0/17)
P40: LANCAR (0/22)
P41: LANCAR (0/17)
P42: LANCAR (0/23)
P43: LANCAR (0/21)
P44: LANCAR (0/21)
P45: LANCAR (0/23)
P46: LANCAR (0/17)
P47: LANCAR (0/21)
P48: LANCAR (0/25)
P49: LANCAR (0/28)
P50: LANCAR (0/18)
P51: LANCAR (0/27)
P52: LANCAR (0/20)
P53: LANCAR (0/21)
P54: LANCAR (0/27)
P55: LANCAR (0/18)
P56: LANCAR (0/18)
P57: LANCAR (0/20)
P58: LANCAR (0/24)
P59: LANCAR (0/27)
P60: LANCAR (0/19)
P61: LANCAR (0/20)
P62: LANCAR (0/27)
P63: LANCAR (0/29)
P64: LANCAR (0/26)
P65: LANCAR (0/23)
P66: LANCAR (0/27)
P67: LANCAR (0/18)
P68: LANCAR (0/17)
P69: LANCAR (0/24)
P70: LANCAR (0/18)
P71: LANCAR (0/24)
P72: LANCAR (0/18)
P73: LANCAR (0/22)
P74: LANCAR (0/27)
P75: LANCAR (0/19)
P76: LANCAR (0/23)
P77: LANCAR (0/24)
P78: LANCAR (0/18)
P79: LANCAR (0/22)
P80: LANCAR (0/26)
P81: LANCAR (0/24)
P82: LANCAR (0/25)
P83: LANCAR (0/23)
P84: LANCAR (0/28)
P85: LANCAR (0/16)
P86: LANCAR (0/22)
P87: LANCAR (0/28)
P88: LANCAR (0/21)
P89: LANCAR (0/15)
P90: LANCAR (0/29)
P91: LANCAR (0/19)
P92: LANCAR (0/15)
P93: LANCAR (0/17)
P94: LANCAR (0/29)
P95: LANCAR (0/20)
P96: LANCAR (0/15)
P97: LANCAR (0/24)
P98: LANCAR (0/15)
P99: LANCAR (0/23)
Big-O: O(n)
>> ISOLASI
Rollback: ('P11', 'TIMUR', 1779338089.200555) | Big-O: O(1)
>> KELUAR
PS C:\Users\ASUS\OneDrive\ドキュメント\arwan codingan>

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modul_2_priority_queue import PriorityQueueKendaraan, Kendaraan

def test_enqueue_priority():
    pq = PriorityQueueKendaraan()
    motor = Kendaraan(1, 4, "P01", "-", 0)
    ambulance = Kendaraan(2, 1, "P01", "-", 0)
    bus = Kendaraan(3, 2, "P01", "-", 0)
    pq.enqueue(motor)
    pq.enqueue(ambulance)
    pq.enqueue(bus)
    # urutan keluar: ambulance (1), bus (2), motor (4)
    assert pq.dequeue().jenis == 1
    assert pq.dequeue().jenis == 2
    assert pq.dequeue().jenis == 4

def test_fifo_same_priority():
    pq = PriorityQueueKendaraan()
    k1 = Kendaraan(1, 3, "", "", 0)
    k2 = Kendaraan(2, 3, "", "", 0)
    pq.enqueue(k1)
    pq.enqueue(k2)
    assert pq.dequeue().id_kendaraan == 1
    assert pq.dequeue().id_kendaraan == 2

def test_len():
    pq = PriorityQueueKendaraan()
    assert len(pq) == 0
    pq.enqueue(Kendaraan(1, 1, "", "", 0))
    assert len(pq) == 1
    pq.dequeue()
    assert len(pq) == 0

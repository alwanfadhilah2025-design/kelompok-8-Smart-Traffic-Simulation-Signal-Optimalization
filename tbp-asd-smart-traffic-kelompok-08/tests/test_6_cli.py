import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modul_6_cli import JENIS_KENDARAAN, ARAH, Stack
from src.modul_1_graph import GraphJalan, Persimpangan, generate_jaringan
from src.modul_2_priority_queue import PriorityQueueKendaraan, Kendaraan
from src.modul_3_dijkstra import dijkstra_rute
from src.modul_4_bst_index import BSTJalan
from src.modul_5_sorting import selection_sort_by_queue_length


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() is None


def test_generate_jaringan_cli():
    persimpangan, edges = generate_jaringan(25, 17)
    assert len(persimpangan) == 25
    assert len(edges) >= 39


def test_integration_queue():
    q = PriorityQueueKendaraan()
    k = Kendaraan(1, JENIS_KENDARAAN['MOBIL'], "P01", "-", 0)
    q.enqueue(k)
    assert len(q) == 1
    out = q.dequeue()
    assert out.id_kendaraan == 1

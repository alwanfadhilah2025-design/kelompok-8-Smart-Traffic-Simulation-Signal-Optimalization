import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modul_1_graph import GraphJalan, Persimpangan, generate_jaringan

def test_tambah_persimpangan():
    g = GraphJalan()
    p = Persimpangan("P01", 20)
    g.tambah_persimpangan(p)
    assert "P01" in g.adj
    assert g.persimpangan["P01"] == p

def test_tambah_jalan_dua_arah():
    g = GraphJalan()
    g.tambah_persimpangan(Persimpangan("A"))
    g.tambah_persimpangan(Persimpangan("B"))
    g.tambah_jalan("A", "B", 500, 2, dua_arah=True)
    tetangga_A = g.tetangga("A")
    assert len(tetangga_A) == 1
    assert tetangga_A[0][0] == "B"
    tetangga_B = g.tetangga("B")
    assert len(tetangga_B) == 1
    assert tetangga_B[0][0] == "A"

def test_generate_jaringan():
    persimpangan, edges = generate_jaringan(25, 17)
    assert len(persimpangan) == 25
    assert len(edges) >= 39  # 24 + 15 = 39, bisa lebih karena seed
    # Cek tiap edge punya 4 elemen
    for u, v, j, l in edges:
        assert isinstance(j, int)
        assert 100 <= j <= 2000
       

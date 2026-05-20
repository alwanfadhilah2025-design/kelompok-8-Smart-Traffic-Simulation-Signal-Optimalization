import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modul_5_sorting import selection_sort_by_queue_length, insertion_sort_by_queue_length

def test_selection_sort():
    data = [("P02", 5), ("P01", 2), ("P03", 8)]
    sorted_data = selection_sort_by_queue_length(data)
    assert sorted_data == [("P01", 2), ("P02", 5), ("P03", 8)]

def test_insertion_sort():
    data = [("P02", 5), ("P01", 2), ("P03", 8)]
    sorted_data = insertion_sort_by_queue_length(data)
    assert sorted_data == [("P01", 2), ("P02", 5), ("P03", 8)]

def test_sort_empty():
    assert selection_sort_by_queue_length([]) == []
    assert insertion_sort_by_queue_length([]) == []

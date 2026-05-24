from modules.modul5_sorting import (
    selection_sort,
    insertion_sort
)

data = [
    ("P01",3),
    ("P02",8),
    ("P03",1),
    ("P04",5)
]

hasil1 = selection_sort(data)
hasil2 = insertion_sort(data)

print("Selection :", hasil1)
print("Insertion :", hasil2)

assert hasil1[0][1] == 8
assert hasil2[0][1] == 8

print("TEST SORTING BERHASIL")

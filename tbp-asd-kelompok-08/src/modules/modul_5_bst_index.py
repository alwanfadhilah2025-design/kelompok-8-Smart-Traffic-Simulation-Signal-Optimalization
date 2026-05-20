def selection_sort_by_queue_length(queue_data):
    """Selection sort pada list of tuple (nama, panjang_antrian) -> O(n^2)
       Mengurutkan dari antrian terkecil ke terbesar."""
    data = queue_data[:]
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j][1] < data[min_idx][1]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def insertion_sort_by_queue_length(queue_data):
    """Insertion sort pada list of tuple -> O(n^2)"""
    data = queue_data[:]
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and data[j][1] > key[1]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

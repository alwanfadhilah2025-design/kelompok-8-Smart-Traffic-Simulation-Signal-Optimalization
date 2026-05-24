def selection_sort(data):

    arr = data[:]

    n = len(arr)

    for i in range(n):

        idx = i

        for j in range(i + 1, n):

            if arr[j][1] > arr[idx][1]:
                idx = j

        arr[i], arr[idx] = (
            arr[idx],
            arr[i]
        )

    return arr


def insertion_sort(data):

    arr = data[:]

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while (
            j >= 0
            and arr[j][1] < key[1]
        ):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

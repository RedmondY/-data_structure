Left = lambda i: 2 * i + 1
Right = lambda i: 2 * i + 2


def min_heap(arr, i):
    while True:
        left = Left(i)
        right = Right(i)

        if left < heap_size and arr[i] < arr[left]:
            min_index = left
        else:
            min_index = i

        if right < heap_size and arr[min_index] < arr[right]:
            min_index = right

        if min_index == i:
            break

        arr[i], arr[min_index] = arr[min_index], arr[i]

        i = min_index


def build_heap(arr):
    global heap_size
    heap_size = len(arr)
    for i in range(heap_size // 2 - 1, -1, -1):
        min_heap(arr, i)


def heap_sort(arr):
    global heap_size
    heap_size = len(arr)
    build_heap(arr)
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        min_heap(arr, 0)
    return arr


array = [0, 1, 2, 3, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]
sorted_array = heap_sort(array)
print(sorted_array)
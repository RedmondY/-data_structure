Left = lambda i: 2 * i + 1
Right = lambda i: 2 * i + 2


def max_heap(arr, i):
    while True:
        left = Left(i)
        right = Right(i)
        if left < heap_size and arr[i] < arr[left]:
            max_index = left
        else:
            max_index = i
        if right < heap_size and arr[max_index] < arr[right]:
            max_index = right

        if max_index == i:
            break
        else:
            arr[max_index], arr[i] = arr[i], arr[max_index]
        i = max_index


def min_heap(arr, i):
    while True:
        left = Left(i)
        right = Right(i)
        if left < heap_size and arr[i] > arr[left]:
            min_index = left
        else:
            min_index = i

        if right < heap_size and arr[min_index] > arr[right]:
            min_index = right

        if min_index == i:
            break
        arr[min_index], arr[i] = arr[i], arr[min_index]

        i = min_index


def build_heap(arr):
    global heap_size
    heap_size = len(arr)
    for i in range(heap_size // 2, -1, -1):
        # min_heap(arr, i)
        max_heap(arr, i)
    print(arr)


arr = [5, 2, 8, 3, 1, 6, 9]
build_heap(arr)



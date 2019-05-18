def select_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[max_index] < arr[j]:
                max_index = j
        arr[max_index], arr[i] = arr[i], arr[max_index]

    return arr


array = [0, 1, 2, 3, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]
sorted_array = select_sort(array)
print(sorted_array)

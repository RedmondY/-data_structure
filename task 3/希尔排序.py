
def shell_sort(arr):
    n = len(arr)
    gap = n >> 1
    while gap > 0:
        for i in range(gap, n):
            j = i
            while (j - gap) >= 0:
                if arr[j] > arr[j - gap]:
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                    j -= gap
                else:
                    break
        gap >>= 1

    return arr


array = [0, 1, 2, 3, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]
sorted_array = shell_sort(array)
print(sorted_array)

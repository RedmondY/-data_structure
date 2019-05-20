
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


array = [0, 1, 2, 3, 4, 3, 7，8，234，22，1]
sorted_array = bubble_sort(array)
print(sorted_array)

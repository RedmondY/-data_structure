def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    arr = merge(left, right)
    return arr


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    if i == len(left):
        for num in right[j:]:
            result.append(num)

    if j == len(right):
        for num in left[i:]:
            result.append(num)

    return result


array = [0, 1, 2, 3, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]
sorted_array = merge_sort(array)
print(sorted_array)

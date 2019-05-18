def qsort(arr, start, end):
    base = arr[start]
    pl = start
    pr = end
    while pl < pr:
        while pl < pr and arr[pr] <= base:
            pr -= 1
        if pl == pr:
            break
        else:
            arr[pl], arr[pr] = arr[pr], arr[pl]

        while pl < pr and arr[pl] >= base:
            pl += 1
        if pl == pr:
            break
        else:
            arr[pl], arr[pr] = arr[pr], arr[pl]

    # now pl == pr
    if pl - 1 > start:
        qsort(arr, start, pl - 1)
    if pr + 1 < end:
        qsort(arr, pr + 1, end)

    return arr


array = [0, 1, 2, 3, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]
sorted_array = qsort(array, 0, len(array) - 1)
print(sorted_array)

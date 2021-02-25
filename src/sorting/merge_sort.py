def sorting(array: [], start: int, end: int):
    # print('before sorting: ', array)
    print('s={}, e={}, arr={}'.format(start, end, array))
    if end - start < 2:
        print('s={}, e={} returned ....')
        return array[start]
    mid = (start + end) // 2
    sorting(array, start, mid)
    sorting(array, mid, end)
    merging(array, start, mid, end)
    print('after sorting: ', array)


def merging(array: [], start: int, mid: int, end: int):
    if array[mid - 1] <= array[mid]:
        return
    i = start
    j = mid
    temp_index = 0
    temp_arr = [-1] * (end - start)
    while i < mid and j < end:
        if array[i] <= array[j]:
            temp_arr[temp_index] = array[i]
            i += 1
        else:
            temp_arr[temp_index] = array[j]
            j += 1
        temp_index += 1

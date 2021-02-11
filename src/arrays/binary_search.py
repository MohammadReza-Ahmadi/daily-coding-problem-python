def binary_search(array: [], l, h, target: int):
    print('loop..')
    if h < l:
        return -1

    m = l + (((h - l) + 1) // 2)
    if array[l] == target:
        return l
    elif array[h] == target:
        return h
    elif array[m] == target:
        return m
    elif array[m] > target:
        h = m - 1
        return binary_search(array, l, h, target)
    else:
        l = m + 1
        return binary_search(array, l, h, target)

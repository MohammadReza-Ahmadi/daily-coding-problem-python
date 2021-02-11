def m1_find_missing_element_by_binary_search(arr1: [], arr2: [], l1, l2, h1, h2):
    print('loop..')
    if h1 < l1 or h2 < l2:
        return -1

    m1 = l1 + (((h1 - l1) + 1) // 2)
    m2 = l2 + (((h2 - l2) + 1) // 2)
    if arr1[l1] != arr2[l2]:
        return arr1[l1]
    if arr1[h1] != arr2[h2]:
        return arr1[h1]
    if arr1[m1] != arr2[m2]:
        return arr1[m1]
    elif arr1[m1] > arr2[m2]:
        h1 = m1 - 1
        h2 = m2 - 1
        return m1_find_missing_element_by_binary_search(arr1, arr2, l1, l2, h1, h2)
    else:
        l1 = m1 + 1
        l2 = m2 + 1
        return m1_find_missing_element_by_binary_search(arr1, arr2, l1, l2, h1, h2)


def m2_find_missing_element_by_binary_search(arr1: [], arr2: [], l, h):
    print('loop..')
    if h < l:
        return -1

    m = l + (((h - l) + 1) // 2)
    if arr1[l] != arr2[l]:
        return arr1[l]
    elif h == len(arr2) or arr1[h] != arr2[h]:
        return arr1[h]
    elif arr1[m] != arr2[m]:
        return arr1[m]
    elif arr1[m] > arr2[m]:
        h = m - 1
        return m2_find_missing_element_by_binary_search(arr1, arr2, l, h)
    else:
        l = m + 1
        return m2_find_missing_element_by_binary_search(arr1, arr2, l, h)

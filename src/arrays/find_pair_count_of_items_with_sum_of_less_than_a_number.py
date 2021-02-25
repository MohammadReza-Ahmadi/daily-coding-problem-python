def find_count_of_pairs(arr: [], x: int) -> int:
    c = 0
    s = len(arr) - 1
    i = s
    j = 0
    print(arr)
    while i > j:
        if arr[i] + arr[j] < x:
            print('{},{} - c={}'.format(arr[i], arr[j], (i - j)))
            c += (i - j)
            j += 1
        else:
            i -= 1
    return c

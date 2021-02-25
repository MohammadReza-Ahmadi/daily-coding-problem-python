def get_maximum_sum_of_subsequence(array: []) -> []:
    s = len(array)
    lis = array.copy()
    print(array)
    for i in range(0, s):
        for j in range(i + 1, s):
            if array[j] > array[i] and (lis[i] + array[j]) > lis[j]:
                lis[j] = lis[i] + array[j]
                print('({}, {}) -> lis[{}]={}'.format(array[i], array[j], j, lis[j]))
    # get max value
    mx = 0
    for n in range(s):
        if lis[n] > mx:
            mx = lis[n]
    return mx

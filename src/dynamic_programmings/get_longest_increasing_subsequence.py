def get_longest_subsequence(array: []) -> []:
    s = len(array)
    lis = [1] * s
    for i in range(s):
        for j in range(i + 1, s):
            if array[j] > array[i] and lis[i] + 1 > lis[j]:
                lis[j] = lis[i] + 1
    # get max value
    mx = 1
    for n in range(s):
        if lis[n] > mx:
            mx = lis[n]
    return mx

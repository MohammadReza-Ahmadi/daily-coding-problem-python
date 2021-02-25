def find_fair_index(arr1: [], arr2: []):
    a1_sum = 0
    a2_sum = 0
    for i in range(len(arr1)):
        a1_sum += arr1[i]
        a2_sum += arr2[i]

    if a1_sum != a2_sum:
        print('there is no fair-index for arrays!')
        return 0
    s = 0
    for i in range(len(arr1)):
        s += arr1[i]
        if a1_sum == 2 * s and i < (len(arr1) - 1):
            print('the fair-index is {}'.format(i+1))
            return i + 1

    print('there is no fair-index for arrays!')
    return 0

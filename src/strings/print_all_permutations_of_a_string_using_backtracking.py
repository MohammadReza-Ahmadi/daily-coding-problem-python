def tostring(a):
    return ''.join(a)


def permute(a, l, r):
    if l == r:
        print(tostring(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


if __name__ == '__main__':
    string = 'ABCDE'
    n = len(string) - 1
    a = list(string)
    permute(a, 0, n)
    # given_list = list(string)
    # print(given_list)
    # print(tostring(given_list))

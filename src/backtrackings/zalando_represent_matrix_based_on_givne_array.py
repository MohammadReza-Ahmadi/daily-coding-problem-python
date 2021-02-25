def get_matrix(u: int, l: int, arr: []) -> str:
    s = 0
    for i in range(len(arr)):
        s += arr[i]
    if s != (u + l):
        return 'IMPOSSIBLE'

    print('arr={}, u={}, l={}'.format(arr, u, l))
    mu = get_matrix_recursive(u, l, arr, 0, '')
    ml = get_matrix_recursive(u, l, arr, 0, '')
    print('mu={}'.format(mu))
    print('ml={}'.format(ml))
    return mu + ',' + ml


def get_matrix_recursive(u: int, l: int, arr: [], i, m: str) -> {}:
    if i >= len(arr):
        if u != 0 or l != 0:
            return 'IMPOSSIBLE'
        return m

    if arr[i] == 0:
        r1 = get_matrix_recursive(u, l, arr, i + 1, m + '0')
        r2 = get_matrix_recursive(u, l, arr, i + 1, m + '0')
        return r1 + r2
    elif arr[i] == 1:
        r1 = get_matrix_recursive(u - 1, l, arr, i + 1, m + '1')
        r2 = get_matrix_recursive(u, l, arr, i + 1, m + '0')
        if r1.__eq__('IMPOSSIBLE') or r2.__eq__('IMPOSSIBLE'):
            r1 = get_matrix_recursive(u, l, arr, i + 1, m + '0')
            r2 = get_matrix_recursive(u, l - 1, arr, i + 1, m + '1')
    else:
        r1 = get_matrix_recursive(u - 1, l, arr, i + 1, m + '1')
        r2 = get_matrix_recursive(u, l - 1, arr, i + 1, m + '1')

    return r1 + r2

#  single line version , its ok
# def get_matrix_recursive(b: int, arr: [], i, m: str) -> str:
#     if i >= len(arr):
#         if b != 0:
#             return 'IMPOSSIBLE'
#         return m
#
#     if arr[i] == 0:
#         return get_matrix_recursive(b, arr, i + 1, m + '0')
#     else:
#         r = get_matrix_recursive(b - 1, arr, i + 1, m + '1')
#         if arr[i] == 1 and r.__eq__('IMPOSSIBLE'):
#             r = get_matrix_recursive(b, arr, i + 1, m + '0')
#         return r

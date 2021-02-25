def primality(n):
    return check_primality(n, 2, n)


# d = divisor
def check_primality(n, d, x):
    if n == 1:
        return 'Not prime'
    if d >= x:
        return 'Prime'

    if n % d == 0:
        return 'Not prime'
    x = n // 2
    return check_primality(n, d + 1, x)

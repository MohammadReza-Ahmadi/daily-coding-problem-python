def get_minimal_difference(A):
    s = 0
    f = 0
    for a in A:
        s += a
    m = s
    for a in range(len(A) - 1):
        s -= A[a]
        f += A[a]
        if abs(s - f) < m:
            m = abs(s - f)
    return m

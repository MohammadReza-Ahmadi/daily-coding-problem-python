def step_perms_by_recursion(n):
    cache = dict()
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n not in cache:
        cache[n] = step_perms_by_recursion(n - 1) + step_perms_by_recursion(n - 2) + step_perms_by_recursion(n - 3)
    return cache[n]

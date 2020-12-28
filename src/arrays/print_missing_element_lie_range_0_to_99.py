def get_missing_numbers(array):
    print(array)
    seen = [0] * 100
    for i in range(len(array)):
        if array[i] < 100:
            seen[array[i]] = 1
    i = 0
    while i < 100:
        if not seen[i]:
            j = i + 1
            while j < 100 and not seen[j]:
                j += 1

            # ternary operator:
            # [on_true] if [expression] else [on_false]
            print(i) if i + 1 == j else print(i, '-', j - 1)
            i = j
        else:
            i += 1

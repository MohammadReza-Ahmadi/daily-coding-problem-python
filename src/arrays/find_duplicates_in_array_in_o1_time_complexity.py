def find_duplicates(array: []) -> []:
    dup = []
    for a in array:
        if array[a] > (len(array) - 1):
            continue
        elif array[a] < 0:
            dup.append(abs(array[0]))
        else:
            array[a] = -array[a]
    return dup

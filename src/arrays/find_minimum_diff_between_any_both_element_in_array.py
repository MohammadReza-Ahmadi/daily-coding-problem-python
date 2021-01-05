from typing import List


def find_min_diff(array: []):
    if len(array) == 1:
        return 0

    List.sort(array)
    min_diff = array[1] - array[0]
    for i in range(1, len(array)):
        if i < len(array) - 1 and (array[i + 1] - array[i]) < min_diff:
            min_diff = array[i + 1] - array[i]

    return min_diff

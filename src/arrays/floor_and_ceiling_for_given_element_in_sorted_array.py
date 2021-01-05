def get_floor_and_ceiling_of_array_m1_linear_search(array: [], x: int):
    #     floor,ceil
    ret = [-1, -1]
    if x < array[0]:
        ret[1] = array[0]
        return ret
    elif x > array[len(array) - 1]:
        ret[0] = array[len(array)-1]
        return ret

    for i in range(len(array)):
        if array[i] == x:
            ret[0] = ret[1] = array[i]
            return ret

        if i < len(array) - 1 and array[i] < x < array[i + 1]:
            ret[0] = array[i]
            ret[1] = array[i + 1]
            return ret
    return ret


def get_floor_and_ceiling_of_array_m2_binary_search(array: [], x: int):
    ret = [-1, -1]
    if x < array[0]:
        ret[1] = array[0]
        return ret
    if x > array[len(array) - 1]:
        ret[0] = array[len(array) - 1]
        return ret
    return m2_helper(array, x, 0, len(array) - 1)


def m2_helper(array: [], x: int, low: int, high: int):
    # array = [1, 2, 8, 10, 10, 12, 19]
    ret = [-1, -1]
    if low > high:
        return ret

    if x == array[low] or x == array[high]:
        ret[0] = ret[1] = x
        return ret
    else:
        mid = ((high - low) + 1) // 2
        if x == array[mid]:
            ret[0] = ret[1] = x
            return ret
        elif array[mid] < x:
            if x <= array[mid + 1]:
                ret[0] = array[mid]
                ret[1] = array[mid + 1]
                return ret
            else:
                return m2_helper(array, x, mid + 2, high)
        else:
            if array[mid - 1] < x:
                ret[0] = array[mid - 1]
                ret[1] = array[mid]
                return ret
            else:
                return m2_helper(array, x, low, mid - 1)

def get_floor_and_ceiling_of_array_m1_linear_search(array: [], x: int):
    #     floor,ceil
    ret = [-1, -1]
    if x < array[0]:
        ret[0] = -1
        ret[1] = array[0]
        return ret

    for i in range(len(array)):
        if array[i] == x:
            ret[0] = array[i]
            ret[1] = array[i]
            return ret

        if array[i] < x < array[i + 1]:
            ret[0] = array[i]
            ret[1] = array[i + 1]
            return ret
    return ret


def get_floor_and_ceiling_of_array_m1_binary_search(array: [], x: int):
    print()
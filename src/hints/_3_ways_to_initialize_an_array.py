import numpy as np


# initialize an array with defined size and default value
def first_way():
    # [value for element in range(num)]
    arr = []
    print("before initialize:")
    print(arr)
    arr = [-1 for i in range(100)]
    print("after initialize:")
    print(arr)


def second_way():
    arr = []
    print("before initialize:")
    print(arr)
    # arr = [default_value] * size
    arr = [-1] * 100
    print("after initialize:")
    print(arr)


def third_way():
    # numpy.empty(size, dtype=object)
    arr = np.empty(100, dtype=object)
    print(arr)


if __name__ == '__main__':
    # first_way()
    second_way()
    # third_way()

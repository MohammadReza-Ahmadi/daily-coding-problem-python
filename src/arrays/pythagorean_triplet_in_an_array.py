# print("hello")

# for x in range(4, 7):
#     print(x)


class PythagoreanTripletInAnArray:
    def find_triplet(self, array):
        for x in range(array.__len__()):
            array[x] = array[x] ** 2

        array.sort()
        for i in range(len(array) - 1, 2, -1):
            l = 0
            r = i - 1
            while l < r:
                if array[l] + array[r] == array[i]:
                    return True

                if array[l] + array[r] < array[i]:
                    l += 1
                else:
                    r -= 1
        return False


# c = PythagoreanTripletInAnArray()
# array = [3, 1, 4, 6, 5]
# print(c.findTriplet(array))

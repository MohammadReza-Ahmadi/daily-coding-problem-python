class SegregateOnesAndZerosInAnArray:
    def do_segregate(self, array):
        l = 0
        r = len(array) - 1
        while l < r:
            while array[l] == 0 and l < r:
                l += 1

            while array[r] == 1 and l < r:
                r -= 1

            if l < r:
                array[l] = 0
                array[r] = 1
                l += 1
                r -= 1
        return array


c = SegregateOnesAndZerosInAnArray()
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
c.do_segregate(arr)
print(arr)

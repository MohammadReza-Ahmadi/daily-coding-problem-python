class CheckForPairByGivenSumInAnArray:
    def has_pair_m1(self, array, sum):
        l = 0
        r = len(array) - 1
        array.sort()
        while l < r:
            if array[l] + array[r] == sum:
                return True
            elif array[l] + array[r] < sum:
                l += 1
            else:
                r -= 1
        return False

    def has_pair_m2(self, array, sum):
        dict = {12: 1}
        for i in range(len(array)):
            temp = sum - array[i]
            if temp >= 0 and bool(dict.get(temp)) and dict[temp] == 1:
                return True
            else:
                dict[array[i]] = 1

        return False


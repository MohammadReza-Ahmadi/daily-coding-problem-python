# Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.
#
# Example
# arr = [4,6,4,5,6,2]
#
# She gives the students candy in the following minimal amounts:[1,2,1,2,3,1] . She must buy a minimum of 10 candies.
#
# Function Description
#
# Complete the candies function in the editor below.
#
# candies has the following parameter(s):
#
# int n: the number of children in the class
# int arr[n]: the ratings of each student
# Returns
#
# int: the minimum number of candies Alice must buy
# Input Format
#
# The first line contains an integer, , the size of .
# Each of the next  lines contains an integer  indicating the rating of the student at position .
#
# Constraints
#
# Sample Input 0
#
# 3
# 1
# 2
# 2
# Sample Output 0
#
# 4

# def candies(n, arr):
#     for i in range(n):


def candies_recursive_greedy(arr, i, b):
    if i == (len(arr) - 1):
        return
    if i==0 or arr[i] == arr[i - 1]:
        r = candies_recursive_greedy(arr, i + 1, 1)
        if r == 0:
           r = candies_recursive_greedy(arr, i + 1, b + 2)

    elif arr[i] > arr[i - 1]:
        r = candies_recursive_greedy(arr, i + 1, b + 1)
        if r == 0:
           r = candies_recursive_greedy(arr, i + 1, b + 2)
        return r
    else:
        if b == 1:
            return 0
        else:
            r = candies_recursive_greedy(arr, i + 1, b - 1)
            if r==-1:
                candies_recursive_greedy(arr, i + 1, b - 1)

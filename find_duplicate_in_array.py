# Find Duplicates in Array:
# https://www.interviewbit.com/problems/find-duplicate-in-array/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A_set = set()
        for num in A:
            if num in A_set:
                return num
            A_set.add(num)
        return -1

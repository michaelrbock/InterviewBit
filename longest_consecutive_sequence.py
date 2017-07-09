# Problem description:
# https://www.interviewbit.com/problems/longest-consecutive-sequence/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        A_set = set(A)
        max_length = 1
        for num in A:
            if num - 1 not in A_set:
                curr = num + 1
                while curr in A_set:
                    curr += 1
                max_length = max(max_length, curr - num)
        return max_length

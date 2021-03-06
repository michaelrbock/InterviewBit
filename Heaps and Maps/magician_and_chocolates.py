# Magician and Chocolates:
# https://www.interviewbit.com/problems/magician-and-chocolates/

import heapq

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        # Invert bag sizes to use min heap impl.
        bags = [-1 * bag for bag in B]
        heapq.heapify(bags)

        result = 0
        for i in xrange(A):
            largest_bag = heapq.heapreplace(bags, ((bags[0] * -1) / 2) * -1)
            result += (largest_bag * -1)

        return result % 1000000007

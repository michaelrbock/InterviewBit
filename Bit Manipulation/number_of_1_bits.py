# Number of 1 Bits:
# https://www.interviewbit.com/problems/number-of-1-bits/

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        bits = 0
        mask = 1
        for i in xrange(32):
            if A & mask != 0:
                bits += 1
            mask <<= 1
        return bits

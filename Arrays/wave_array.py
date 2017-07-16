# Wave Array:
# https://www.interviewbit.com/problems/wave-array/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        sorted_A = sorted(A)
        
        for i in xrange(len(sorted_A) - 1):
            # even index, needs to be >= next
            if i % 2 == 0:
                if sorted_A[i] < sorted_A[i + 1]:
                    sorted_A[i], sorted_A[i + 1] = sorted_A[i + 1], sorted_A[i]
            # odd index, needs to be <= next
            else:
                if sorted_A[i] > sorted_A[i + 1]:
                    sorted_A[i], sorted_A[i + 1] = sorted_A[i + 1], sorted_A[i]

        return sorted_A

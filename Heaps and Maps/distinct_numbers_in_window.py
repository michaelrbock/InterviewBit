# Distinct Numbers in Window:
# https://www.interviewbit.com/problems/distinct-numbers-in-window/

from collections import Counter

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        result = []
        if B > len(A):
            return result

        # Use negative numbers to get max heap from min heapq impl.
        counter = Counter(A[:B])
        result.append(len(counter))
        for index in xrange(B, len(A)):
            counter[A[index - B]] -= 1
            if counter[A[index - B]] == 0:
                del counter[A[index - B]]
            counter[A[index]] += 1
            result.append(len(counter))

        return result

# Sorted Insert Position:
# https://www.interviewbit.com/problems/sorted-insert-position/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        lower = 0
        upper = len(A)
        mid = lower + (upper - lower) // 2
        while lower < upper:
            mid = lower + (upper - lower) // 2
            if B == A[mid]:
                return mid
            elif B > A[mid]:
                if lower == mid:
                    return mid + 1
                lower = mid
            elif B < A[mid]:
                upper = mid
        return mid

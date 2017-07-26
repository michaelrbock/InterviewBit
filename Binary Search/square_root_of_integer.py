# Square Root of Integer:
# https://www.interviewbit.com/problems/square-root-of-integer/

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A <= 1:
            return A

        lower = 1
        upper = A
        result = 1
        while lower <= upper:
            mid = (lower + upper) / 2
            if mid * mid == A:
                return mid

            if mid * mid < A:
                lower = mid + 1
                result = mid
            else:  # mid * mid >= A
                upper = mid - 1

        return result

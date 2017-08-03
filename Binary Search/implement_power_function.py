# Implement Power Function:
# https://www.interviewbit.com/problems/implement-power-function/

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if n == 0:
            return 1 % d
        temp = self.pow(x, n/2, d)
        if n % 2 == 0:
            return (temp * temp) % d
        else:
            if n > 0:
                return (x * temp * temp) % d
            else:
                return ((temp * temp) / x) % d

# Minimum Characters required to make a String Palindromic:
# https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/

def is_palindrome(string):
        return string == string[::-1]

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # protect against empty string
        # is_palindrome("") == True
        if not A:
            return 0
        # idea: how many chars do we need
        # to remove from the end until it's
        # a palindrome?
        for i in xrange(len(A), -1, -1):
            if is_palindrome(A[0:i]):
                return len(A) - i

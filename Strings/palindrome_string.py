# Palindrome String:
# https://www.interviewbit.com/problems/palindrome-string/

class Solution:
    # @param A : string
    # @return an integer (0 for False, 1 for True)
    def isPalindrome(self, A):
        if len(A) <= 1:
            return 1
        
        first = 0
        second = len(A) - 1
        while True:
            while not A[first].isalnum() and first < len(A) - 1:
                first += 1
            while not A[second].isalnum() and second >= 1:
                second -= 1
            if first >= second:
                break
            if A[first].lower() != A[second].lower():
                return 0
            first += 1
            second -= 1

        return 1

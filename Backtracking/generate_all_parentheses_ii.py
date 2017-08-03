# Generate all Parentheses II:
# https://www.interviewbit.com/problems/generate-all-parentheses-ii/

def paren(left, right):
    if left == right == 0:
        yield ""
    else:
        if left > 0:
            for p in paren(left - 1, right):
                yield "(" + p

        if right > left:
            for p in paren(left, right - 1):
                yield ")" + p


class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        if A == 0:
            return []
        return [x for x in paren(A, A)]

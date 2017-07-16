# Roman To Integer
# https://www.interviewbit.com/problems/roman-to-integer/

_TOKEN_TO_VALUE = {
    'I': 1,  'V': 5,   'X': 10,
    'L': 50, 'C': 100, 'D': 500,
    'M': 1000
}

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        curr = 0
        total = 0
        for token in A:
            value = _TOKEN_TO_VALUE[token]
            # If prev tokens apply to later num
            if value > curr and curr != 0:
                total += (value - curr)
                curr = 0
            elif value < curr:
                total += curr
                curr = value
            else:
                curr += value
        # If there's anything else left in curr:
        total += curr
        return total

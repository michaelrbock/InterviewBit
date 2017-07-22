# Substring Concatenation
# https://www.interviewbit.com/problems/substring-concatenation/

from collections import Counter

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        result = []
        if not A or not B:
            return result

        num_words = len(B)
        word_len = len(B[0])
        word_count = Counter(B)

        for i in xrange(len(A) - (num_words * word_len) + 1):
            target = Counter(word_count)
            j = i
            while j <= len(A) - word_len and len(target) != 0:
                sub = A[j:j + word_len]
                j += word_len
                if sub not in target:
                    break
                elif target[sub] > 1:
                    target[sub] -= 1
                else:
                    del target[sub]

            if len(target) == 0:
                result.append(i)
        
        return result

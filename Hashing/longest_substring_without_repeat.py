# Longest Substring Without Repeat:
# https://www.interviewbit.com/problems/longest-substring-without-repeat/

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        chars = {}  # char to prev index in A
        max_len = 0
        count = 0
        prev = 0

        for index, char in enumerate(A):
            if char in chars:
                prev = chars[char]
                count = min(count + 1, index - prev)
                chars[char] = index
            else:
                count += 1
                chars[char] = index
            max_len = max(max_len, count)
        
        return max_len

# Length of Last Word:
# https://www.interviewbit.com/problems/length-of-last-word/

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        words = []  # list of all the words
        word = []  # build up words as char arrays
        for c in A:
            if c == ' ' and word:
                words.append(word)
                word = []
            elif c != ' ':
                word.append(c)
        if word:
            words.append(word)
        return len(words[-1]) if words else 0

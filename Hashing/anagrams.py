# Anagrams:
# https://www.interviewbit.com/problems/anagrams/

from collections import defaultdict

def _char_count(word):
    """Returns a hashable version of char counts dict for word."""
    counts = defaultdict(int)
    for char in word:
        counts[char] += 1
    return tuple(sorted(counts.iteritems()))


class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        words = defaultdict(list) # char_count dicts to list of index + 1
        for index, word in enumerate(A):
            char_count = _char_count(word)
            words[char_count].append(index + 1)
            
        return words.values()

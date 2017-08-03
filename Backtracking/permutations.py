# Permutations:
# https://www.interviewbit.com/problems/permutations/

def perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in perms(elements[1:]):
            for i in xrange(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        return [x for x in perms(A)]

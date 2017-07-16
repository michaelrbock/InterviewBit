# Remove Duplicates from Sorted ArrayBookmark Suggest Edit
# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 1:
            return len(A)
            
        dupes = 0
        
        for i in xrange(len(A) - 1):
            if A[i] != A[i+1]:
                A[dupes] = A[i]
                dupes += 1
        
        A[dupes] = A[-1]
        dupes += 1
        
        return dupes

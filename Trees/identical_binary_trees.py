# Identical Binary Trees:
# https://www.interviewbit.com/problems/identical-binary-trees/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if not A and not B:
            return True
        elif (A and not B) or (B and not A):
            return False
        elif not A.left and not A.right and not B.left and not B.right:
            return A.val == B.val
        elif not A.left and not B.left:
            return self.isSameTree(A.right, B.right)
        elif not A.right and not B.right:
            return self.isSameTree(A.left, B.left)
        else:
            return self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)

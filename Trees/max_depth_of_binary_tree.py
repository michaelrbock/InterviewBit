# Max Depth of Binary Tree:
# https://www.interviewbit.com/problems/max-depth-of-binary-tree/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if not A.left and not A.right:
            return 1
        elif not A.left:
            return 1 + self.maxDepth(A.right)
        elif not A.right:
            return 1 + self.maxDepth(A.left)
        else:
            return 1+ max(self.maxDepth(A.left), self.maxDepth(A.right))

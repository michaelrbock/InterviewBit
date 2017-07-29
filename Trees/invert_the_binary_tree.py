# Invert the Binary Tree:
# https://www.interviewbit.com/problems/invert-the-binary-tree/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
        if not root:
            return root

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.right = left
        root.left = right

        return root

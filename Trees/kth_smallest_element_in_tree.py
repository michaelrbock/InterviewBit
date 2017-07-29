# Kth Smallest Element In Tree:
# https://www.interviewbit.com/problems/kth-smallest-element-in-tree/#

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def kthsmallest(self, root, k):
        curr = root
        stack = []
        count = 0
        
        while curr:
            stack.append(curr)
            curr = curr.left

        while stack:
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

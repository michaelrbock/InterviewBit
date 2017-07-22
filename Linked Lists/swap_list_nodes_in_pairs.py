# Swap List Nodes in pairs
# https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if not A or not A.next:
            return A

        prev = None
        curr = A
        result = A.next

        while curr and curr.next:
            # Do swap
            if prev:
                prev.next = curr.next
            temp = curr.next
            curr.next = temp.next
            temp.next = curr

            # Move on
            prev = curr
            curr = curr.next

        return result

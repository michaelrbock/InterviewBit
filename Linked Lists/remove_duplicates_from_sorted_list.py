# Remove Duplicates from Sorted List
# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        curr = A
        while curr and curr.next:
            next_non_dupe = curr
            while next_non_dupe.next and next_non_dupe.val == next_non_dupe.next.val:
                next_non_dupe = next_non_dupe.next
            if curr != next_non_dupe:
                curr.next = next_non_dupe.next
            curr = curr.next
        return A

# Insertion Sort List:
# https://www.interviewbit.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if not A or not A.next:
            return A
        
        head = None
        unsorted = A

        while unsorted:
            curr = unsorted
            unsorted = unsorted.next
            if not head or curr.val < head.val:
                curr.next = head
                head = curr
            else:
                find = head
                while find.next and curr.val > find.next.val:
                    find = find.next
                curr.next = find.next
                find.next = curr

        return head

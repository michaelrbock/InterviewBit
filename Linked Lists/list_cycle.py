# List Cycle:
# https://www.interviewbit.com/problems/list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        fast = A
        slow = A
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow and slow == fast:
                # Now find beginning of cycle:
                slow = A
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

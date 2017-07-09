// Problem description:
// https://www.interviewbit.com/problems/subtract/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::subtract(ListNode* A) {
    // Save a ptr to first node to return.
    ListNode* result = A;

    // Double traverse to get to middle of list.
    ListNode* slow = A; ListNode* fast = A;
    while (fast) {
        if (!fast->next) {
            break;
        }
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // Correct for odd or even, save midpoint if exists.
    ListNode* mid = NULL;
    if (fast) {  // it's odd, slow needs to move over mid point.
        mid = slow;
        slow = slow->next;
    }
    
    // Reverse the second half of the list.
    ListNode* newcurr = NULL; // this will be the head of the split list.
    ListNode* curr = slow;
    while (curr) {
        ListNode* temp = curr->next;
        curr->next = newcurr;
        newcurr = curr;
        curr = temp;
    }
    
    // Do the minus operation while traversing both lists.
    ListNode* first = A; ListNode* second = newcurr;
    while (second) {
        first->val = second->val - first->val;
        if (second->next) {
            first = first->next;
        }
        second = second->next;
    }
    
    // Re-reverse second-half list.
    curr = newcurr;
    newcurr = NULL;  // this will be the head of the split list.
    while (curr) {
        ListNode* temp = curr->next;
        curr->next = newcurr;
        newcurr = curr;
        curr = temp;
    }
    
    // Merge lists.
    if (mid) {
        first->next = mid;
        mid->next = newcurr;
    } else {
        first->next = newcurr;
    }
    
    return result;
}

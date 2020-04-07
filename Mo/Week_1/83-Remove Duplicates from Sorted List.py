"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

    Input: 1->1->2
    Output: 1->2
    
Example 2:

    Input: 1->1->2->3->3
    Output: 1->2->3
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Assign a pointer to the beginning of our list
        pointer_to_head = head 
        
        # while the list is not empty and there is at least 2 elements continue: 
        # Since the list is sorted, if the value is same as the next, assign to 
        # value after, otherwise, simply move pointer forward
        while head != None and head.next != None: 
            if head.val == head.next.val: 
                head.next = head.next.next
            else: 
                head = head.next 
                
        return pointer_to_head
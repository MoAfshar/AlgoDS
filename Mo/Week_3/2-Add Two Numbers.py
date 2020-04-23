"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
# Check for all the edge cases 
# 1 - When the lists are both the same - l1=[1,2,3] l2=[4,5,6]
# 2 - When one lists is longer than the other - l1=[0,1] l2=[0,1,2]
# 3 - When on lists is null - l1=[] l2=[0,1]
# 4 - The sum could have an extra carry of one at the end -l1=[9,9] l2=[1]
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = result = ListNode(None)
        carry = 0
        while l1 or l2 or carry: 
            x = l1.val if l1 else 0 
            y = l2.val if l2 else 0
            _sum = x + y + carry
            if _sum <= 9: 
                result.next = ListNode(_sum)
                carry = 0
            else: 
                r = _sum % 10
                result.next = ListNode(r)
                carry = 1
            if l1: l1 = l1.next 
            if l2: l2 = l2.next 
            result = result.next
        return head.next
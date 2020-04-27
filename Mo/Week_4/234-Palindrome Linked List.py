"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

    Input: 1->2
    Output: false
    
Example 2:

    Input: 1->2->2->1
    Output: true
    
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x): 
        self.val = x
        self.next = None

class Solution:
    # The idea is to reverse the first half (from the middle) and compare it with the second
    # half of the linked list. To do this we will use a slow and fast pointer to be able to 
    # correctly get our pointers in the right place. The fast pointer will simply just move 
    # ahead to help us assign the the slow pointer in the right place
    # This is O(N) time complexity and O(1) space 
    def isPalindrome(self, head: ListNode) -> bool: 
        # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
        reverse = None  
        slow = fast = head 
        # This should reverse the first half of the list correctly 
        while fast and fast.next: 
            # fast traverses faster and moves to the end of the list if the length is odd
            fast = fast.next.next 
            
            reverse_tmp = reverse
            reverse = slow 
            slow = slow.next
            reverse.next = reverse_tmp 
        
        # fast is at the end this is when the linked list is odd, move slow one step further for comparison(cross middle one)
        if fast: 
            slow = slow.next 
        
        # compare the reversed first half with the second half
        while reverse and reverse.val == slow.val: 
            reverse = reverse.next 
            slow = slow.next 
        
        return not reverse
    
    # Loop through the linked list and store all the values in a normal list 
    # Running time O(N) and Space Complexity is O(N) as well
    def isPalindrome2(self, head: ListNode) -> bool:
        values = []
        while head != None: 
            values.append(head.val)
            head = head.next 
        
        start = 0
        end = len(values) - 1
        while start < end: 
            if values[start] != values[end]: 
                return False 
            start += 1
            end -= 1
        return True
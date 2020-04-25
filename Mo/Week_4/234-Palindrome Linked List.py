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
    # Loop through the linked list and store all the values in a normal list 
    # Two pointer method to check whether start and end are equal to each other 
    # Running time O(N) and Space Complexity is O(N) as well
    def isPalindrome(self, head: ListNode) -> bool:
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
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.
    Note:

    Given n will always be valid.

Follow up:
Could you do this in one pass?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First idea that comes to mind is through two passes 
# First pass is to get the length of the linkde list 
# After knowing the length simple ignore the nth node
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head 
        length = 0
        while current is not None: 
            length += 1
            current = current.next 
        # The index for the node that needs to be removed 
        k = length - n 
        # so we know which node to delete 
        prev = None
        ptr = head 
        while k != 0: 
            prev = ptr
            ptr = ptr.next
            k -= 1
        if prev is None: 
            return head.next 
        else: 
            prev.next = ptr.next 
            return head
        
class Solution:
    # One pass algorithm - surpisingly find it easier than the other but both very similar
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_pointer = ListNode(None)
        head_pointer.next = head 
        # Remember these are pointing to None in the beginning
        fast = head_pointer 
        slow = head_pointer 
        
        # This moves the fast pointer to n+1 position i.e at the node we want to remove
        for i in range(0, n+1): 
            fast = fast.next 
            
        while fast is not None: 
            fast = fast.next 
            slow = slow.next 
            
        slow.next = slow.next.next
        return head_pointer.next
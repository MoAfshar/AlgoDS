""""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node which will act as our "new list" which we
        # will appoint the new value to, we will have a pointer "head" to the 
        # beginning of our dummy list so we can return the result of that 
        # list in the end 
        dummy = ListNode(None)
        head = dummy 
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                # If the value is in the first list is smaller than the value in 
                # the second list - put in our "new list" dummy
                dummy.next = l1
                # Now move our pointer to the next element in the first list
                l1 = l1.next
            # We perform the same thing for the other list 
            else:
                dummy.next = l2
                l2 = l2.next 
            # Dont forget to move the dummy pointer, otherwise we would 
            # overwrite the element that is already on there, remember this would
            # store the next value in from the list taken but then we overwrite it 
            # based on the conditions above 
            dummy = dummy.next
            print(dummy)
        
        # If one list larger than the other, append the rest of that list to dummy
        if l1 is None: 
            dummy.next = l2  
        else: 
            dummy.next = l1 
        
        # We return head.next to skip the original "None" node created at the start
        return head.next 

# Note to self: Why do I find Linked list so weird and hard lmao >_<
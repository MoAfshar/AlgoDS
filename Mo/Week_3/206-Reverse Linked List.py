# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# The idea is pretty simple: 
# 1 - Create a new NULL node which we will be point our first node to 
# 2 - Using the head/current node, we iterate through until all nodes in the list until NULL
# 3 - We will store the head's next node refrence in a temp 
# 4 - we will then assign our head to the null node 
# 5 - we will then assign current node to be our temp so we can move the next node successfully 
# 6 - Don't forget to also update our previous node to our current node so we can refrence our 
#     next iteration node successfully to the previous one
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
            previous = None
            current = head
            while current: 
                # current.next, previous, current = previous, current, current.next
                next_tmp = current.next # Remember next node
                current.next = previous # REVERSE! None, first time round.
                previous = current # Used in the next iteration.
                current = next_tmp # Move to next node.
            return previous
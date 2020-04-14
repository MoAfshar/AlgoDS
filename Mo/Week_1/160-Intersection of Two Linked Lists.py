# Write a program to find the node at which the intersection of two singly linked lists begins.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
# Brute Force:
# For each node ai in list A, traverse the entire list B and check if any node in list B coincides with ai.

# First solution that comes to mind using disctionary: 
#   - Iterate through one of the list and store the node object in a dictionary
#   - Iterate through the second list and if the same node object exists in the dictionary return that node
#   - This will be O(N) in time and O(N) in memory - not optimal
#   - Note: Confusing part about this question - the node we are finding will have the same object refrence 
#   - in both of the lists, lists can have the same value but different refrences. However, the intersection 
#   - point means the nodes have the same refrence and the same value.
class Solution:
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = {}
        
        while headA != None: 
            visisted[headA] = None 
            headA = headA.next
        
        while headB != None: 
            if headB in visited: 
                return headB
            headB = headB.next
        return None
    
# The most optimal solution - using the two pointer trick. Looked up the algorithm, it is explained well. 
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB 
        
        while pA != pB: 
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next 
            
        return pA
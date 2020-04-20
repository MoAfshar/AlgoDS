# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # - Two pointer approach - have a fast pointer which moves 2 steps at a time and a slow pointer which 
    #   moves 1 step at a time. If there is a cycle the two pointer will eventually meet. Think of a track. 
    #   if two runners are running, and the track is a cycle, at some point the two runners will meet. 
    #   If their is no cycle then the fast pointer will eventually reach the end and we can return false
    def hasCycle(self, head: ListNode) -> bool: 
        fast = slow = head 
        while fast != None and fast.next != None: 
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast: 
                return True
        return False
        
    # - Store the nodes sequentially in a hashmap and check whether the refrence of a node 
    #   exists already in the list. This not optimal, it is an O(N) time and space complexity 
    def hasCycle2(self, head: ListNode) -> bool:
        visited = {}
        while head != None: 
            if head not in visited: 
                visited[head] = None
                head = head.next
            else: 
                return True 
        return False
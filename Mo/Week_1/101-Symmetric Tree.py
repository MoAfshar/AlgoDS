"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

        1
       / \
      2   2
       \   \
       3    3
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def check(l, r): 
            if l is None and r is None: 
                return True 
            if l is None or r is None: 
                return False 
            if l.val != r.val: 
                return False
            return True
            
        if root is None: 
            return True
        
        left_node, right_node = root.left, root.right
        deq = deque([(left_node, right_node),])
        
        while deq: 
            l, r = deq.popleft()
            if not check(l, r): 
                return False
            if l: 
                deq.append((l.left, r.right))
                deq.append((l.right, r.left))
                
        return True
            
        
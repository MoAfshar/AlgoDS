"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

    Input:     1         1
              / \       / \
             2   3     2   3

            [1,2,3],   [1,2,3]

    Output: true

Example 2:

    Input:     1         1
              /           \
             2             2

            [1,2],     [1,null,2]

    Output: false
    
Example 3:

    Input:     1         1
              / \       / \
             2   1     1   2

            [1,2,1],   [1,1,2]

    Output: false
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None 

class Solution: 
    
    # Using deque we iterate through the tree and check at every stage whether the two nodes are equal 
    # or not, if so we add the child and do the comparisons until the deque is empty 
    def isSameTree(self, p:TreeNode, q: TreeNode) -> bool: 
        
        def check(p, q): 
            if not p and not q: 
                return True 
            if not p or not q: 
                return False 
            if p.val != q.val: 
                return False 
            return True 
        
        deq = deque([(p, q),])
        # while the deq is not empty
        while deq: 
            p, q = deq.popleft()
            if not check(p, q): 
                return False 
            # If p and q is None then we can return True as we have this check covered in our check function
            if p: 
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True
    
    # Recursively check at each step whether the values are the nodes are the same 
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        # If p and q are both None 
        if not p and not q: 
            return True
        # If one of p and q is None 
        if not p or not q: 
            return False
        # If the value of p is not equal to q 
        if p.val != q.val: 
            return False 
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    # Very useful: https://stackoverflow.com/questions/47007680/how-do-and-and-or-act-with-non-boolean-values/47007761#47007761
    # Since and is used, the second expression must also be evaluated if the first is True. Note that, 
    # if the first expression is evaluated to be truthy, the return value is always the result of the 
    # second expression. If the first expression is evaluated to be Falsy, then the result returned is 
    # the result of the first expression.
    
    # Last line could be written as 
    # if self.isSameTree(p.left, q.left):
    #     return self.isSameTree(p.right, q.right)
    # else: 
    #     return self.isSameTree(p.left, q.left)
    
"""    
All values are considered "truthy" except for the following, which are "falsy":

None
False
0
0.0
0j
Decimal(0)
Fraction(0, 1)
[] - an empty list
{} - an empty dict
() - an empty tuple
'' - an empty str
b'' - an empty bytes
set() - an empty set
an empty range, like range(0)
objects for which
obj.__bool__() returns False
obj.__len__() returns 0
"""
    

#--Tried to print out each tree as a string and compare them but doesn't work with printing None--
#-- Decent effort but there is a much easier solution recursively--
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         tree1 = self.check_tree(p, "")
#         tree2 = self.check_tree(q, "")
#         if tree1 == tree2: 
#             return True
        
#         return False
    
#     def check_tree(self, tree: TreeNode, traversal: str) -> list: 
#         if tree != None: 
#             # Root -> Left -> Right
#             traversal += str(tree.val)
#             traversal = self.check_tree(tree.left, traversal)
#             traversal = self.check_tree(tree.right, traversal)
            
#         return traversal 
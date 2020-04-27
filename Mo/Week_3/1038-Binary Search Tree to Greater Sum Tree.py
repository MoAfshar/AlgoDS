# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # In order traversal will gives us the total we need for the greater sum tree 
    # This is a DFS type of traversal which we can use a stack to help us with 
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        total = 0
        current = root
        while stack or current is not None: 
            # We want to traverse all the way down to the right sub tree as this is going to 
            # give us the largest value and go right -> middle -> left 
            while current is not None: 
                stack.append(current)
                current = current.right
            # pop the most recent value (the deepest in the tree) and change the total value
            current = stack.pop()
            total += current.val 
            current.val = total 
            current = current.left 
        
        return root
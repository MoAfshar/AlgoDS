"""
Invert a binary tree.

Example:

Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    
Output:

         4
       /   \
      7     2
     / \   / \
    9   6 3   1
    
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# O(N) time complexity since each node in the tree is visisted/added to the queue once, where n is the number
# of nodes in the tree 
# O(N) space complexity, since in worst case the queue will contain all nodes in one level of the binary tree
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: 
            return None
        
        # Use breadth search style to change the nodes positions at each level by using a queue
        deq = deque([root])
        while deq:
            current = deq.popleft() # Pop current node. First will be the root
            tmp = current.left # Store left in temp so we don't lose refrence 
            current.left = current.right # Swap the left with right
            current.right = tmp # Swap the right with left using our previously stored refrence
            if current.left: deq.append(current.left) # Add the next left node to the queue
            if current.right: deq.append(current.right) # Add the next right node to the queue
            
        return root
    
    # Using recursion 
    def invertTree2(self, root: TreeNode) -> TreeNode: 
        if not root: 
            return None 
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left 
        return root
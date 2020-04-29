"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
              1
             / \
            2   3
           / \     
          4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Count for each node whether a path exists or not
# Perform BFS or DFS to visit each node and keep a counter of the max path found
# O(N) time complexity and O(N) space complexity
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:      
        self.result = 0
        
        def height(root: TreeNode) -> int: 
            if root is None: 
                return 0 
            left = height(root.left)
            right = height(root.right)
            self.result = max(self.result, left+right)
            return max(left, right) + 1
        # Call our function and return our global result which is the path 
        height(root)
        return self.result
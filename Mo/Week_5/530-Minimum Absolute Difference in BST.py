"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

    Input:

       1
        \
         3
        /
       2

    Output:
    1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 
Note:
There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Better solution which solves it in Time Complexity O(n)
# Using Inorder traversal since the tree is a BST, the inorder traversal is sorted
class Solution: 
    def getMinimumDifference(self, root: TreeNode) -> int: 
        if root is None: 
            return 0
        
        stack = []
        previous = 0
        global_min = float(inf)
        while stack or root is not None: 
            while root is not None: 
                stack.append(root)
                root = root.right 
            
            root = stack.pop()
            curr_val = abs(root.val - previous)
            global_min = min(global_min, curr_val)
            previous = root.val
            root = root.left
            
        return global_min
        
        
# First idea: 
# Perfrom BFS O(n) -> store in a list
# sort the list - O(nlogn) 
# Iterate through the list and find the lowest minmum O(n)
# Space O(n) - Time O(nlogn), this basically would work for any type of tree not just BST
class Solution2:
    def getMinimumDifference(self, root: TreeNode) -> int:
        deq = deque([root])
        result = []
        while deq: 
            current = deq.popleft()
            result.append(current.val)
            if current.left: 
                deq.append(current.left)
            if current.right: 
                deq.append(current.right)
        
        result.sort()
        minimum = float(inf)
        for i in range(len(result)-1): 
            res = result[i+1] - result[i]
            minimum = min(minimum, res)
        return minimum
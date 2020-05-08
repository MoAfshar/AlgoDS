"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

    Input: [1,2,3,null,5,null,4]
    Output: [1, 3, 4]
    Explanation:

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
"""
# Definition for a binary tree node.
class TreeNode: 
    def __init__(self, val): 
        self.val = val
        self.left = None
        self.right = None

# The idea is to go throughh the tree in BFS manner 
# At every level we can store each node and return the last node in that level 
# The last node in the level will be the node one the "right side" of the tree
# Time complexity is O(n) and space complexity is O(2n) = o(n)
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        if root is None: 
            return result
        
        deq = deque([root])
        while deq: 
            current_level = []
            for i in range(len(deq)): 
                current = deq.popleft()
                current_level.append(current.val)
                if current.left: 
                    deq.append(current.left)
                if current.right: 
                    deq.append(current.right)
            result.append(current_level.pop()) # O(1)
        return result
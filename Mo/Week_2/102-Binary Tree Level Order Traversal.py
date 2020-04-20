"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
       
    return its level order traversal as:
    [
      [3],
      [9,20],
      [15,7]
    ]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# Use a queue to store the nodes at each level
# Initilise the queue with the root 
# Next check the size of the queue to see how many nodes need processing (max 2)
# Pop the node out of the queue and Add those nodes to a temp list 
# Check whether the node has any children 
# If so add them to the queue 
# Finally append the current level list to the final list 
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None: 
            return result

        deq = deque([root])
        while deq: 
            current_level = []
            for i in range(len(deq)):
                current_node = deq.popleft()
                current_level.append(current_node.val)
                if current_node.left: 
                    deq.append(current_node.left)
                if current_node.right: 
                    deq.append(current_node.right)
            result.append(current_level)
        
        return result
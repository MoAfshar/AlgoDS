"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
    Input:
        3
       / \
      9  20
        /  \
       15   7
       
    Output: [3, 14.5, 11]
    
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Perfrom BFS and calculate the average
    # Time Complexity is O(n) the whole tree is traversed at most once. n refers to the number of nodes 
    # Space complexity is O(m). The size of the qqueue can grow up to at most maximum number of nodes at 
    # any level in the given binary tree. m refers to the maximum number of nodes at any level in the 
    # input tree
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        if not root: 
            return result
        
        deq = deque([root])
        while deq: 
            total = 0
            size = len(deq)
            for _ in range(size): 
                current = deq.popleft()
                total += current.val
                if current.left: 
                    deq.append(current.left)
                if current.right: 
                    deq.append(current.right)
            average = total / size
            result.append(average)
        return result
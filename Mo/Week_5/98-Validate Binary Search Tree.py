# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# More efficient version of in-order traversal 
# O(N) Time (to visit each node in tree) and Space complexity (for stack)
class Solution: 
    def isValidBST(self, root: TreeNode) -> bool: 
        if not root: 
            return True 
        
        stack = []
        current = root 
        previous = float('-inf')
        while stack or current: 
            while current: 
                stack.append(current)
                current = current.left 
            
            current = stack.pop()
            if current.val <= previous: 
                return False 
            previous = current.val
            current = current.right
            
        return True

# Using in-order traversal -> saving the traversal iin a list. 
# Every element in the list must be smaller then previous 
# However there shouldn't be a need to use an extra list -> we can just check current with 
# previous. 
class Solution2: 
    def isValidBST(self, root: TreeNode) -> bool: 
        if not root: 
            return True 
        
        stack, result = [], []
        current = root 
        while stack or current: 
            while current: 
                stack.append(current)
                current = current.left 
            
            current = stack.pop()
            result.append(current)
            current = current.right 
        
        for i in range(len(result)-1): 
            if result[i].val >= result[i+1].val: 
                return False 
        return True

# O(N) time complexity since we visit each node exactly once 
# O(N) space since we keep up to the entire tree 
# Idea is to keep the both upper and lower limits for each node while traversing the tree 
# and compare the node value not with children but with these limits 
class Solution3:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: 
            return True 
        
        deq = deque([(root, float('-inf'), float('inf'))])
        while deq: 
            root, lower, upper = deq.popleft()
            # when we reach the leaf
            if not root: 
                continue 
                
            val = root.val 
            if val <= lower or val >= upper: 
                return False 
            deq.append((root.left, lower, val))
            deq.append((root.right, val, upper))

        return True
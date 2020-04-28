"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
        5
       / \
      3   6
     / \   \
    2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
        5
       / \
      3   6
     / \   \
    2   4   7

Target = 28

Output: False
"""
# Definition for a binary tree node.
class TreeNode: 
    def __init__(self, x): 
        self.val = x
        self.left = None
        self.right = None
        
# We can improve the solution below by performing the compliment as we are traversing the tree instead of
# storing it in a list and traversing once more. 
# As we go node by node we can find the compliment and check whether it exists in a hashmap or not 
# Hence we may find our answer earlier before traversing the whole tree as well as use less space 
# Time complexity is O(n) - n is the number of node and space complexity is O(n), the hashmap can grow atmost upto n
class Solution: 
    def findTarget(self, root: TreeNode, k: int) -> bool: 
        hashmap = {}
        deq = deque([root])
        while deq: 
            current = deq.popleft()
            compliment = k - current.val 
            if compliment in hashmap: 
                return True 
            hashmap[current.val] = compliment
            if current.left: 
                deq.append(current.left)
            if current.right: 
                deq.append(current.right)
        return False

# Initital idea: traverse the binary tree  BST and store it in a list
# Do two sum algorithm with the list
# Time complexity is O(2n) and space complexity is O(2n)
class Solution2:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: 
            return False 
        
        tree = self.traverseBinaryTree(root)
        hashmap = {}
        for i in range(0, len(tree)): 
            compliment = k - tree[i]
            if compliment not in hashmap: 
                hashmap[tree[i]] = compliment 
            else: 
                return True 
        return False

    def traverseBinaryTree(self, root: TreeNode) -> List[int]: 
        deq = deque([root])
        tree = []
        while deq: 
            current = deq.popleft()
            tree.append(current.val)
            if current.left: 
                deq.append(current.left)
            if current.right: 
                deq.append(current.right)
        return tree
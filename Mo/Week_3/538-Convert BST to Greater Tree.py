"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

    Input: The root of a Binary Search Tree like this:
                  5
                /   \
               2     13

    Output: The root of a Greater Tree like this:
                 18
                /   \
              20     13
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Due to the property of BST, we can perform a inorder traversal to visit the nodes from the 
# rightmost tree and add the value of each node to the global total
# To perform an in order traversal we will use a stack which will hold all of the visted nodes
# when the stack is empty it means we have visisted all the nodes
# inorder traversal is one type of DFS search - hence we are using a stack to keep track of the 
# depth in the order we need 
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        stack = []
        node = root
        while stack or node is not None: 
            while node is not None: 
                stack.append(node)
                node = node.right 
                
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
            
        return root
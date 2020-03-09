"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1: 
    Input: "()"
    Output: true
    
Example 2: 
    Input: "()[]{}"
    Output: true   
"""

# Time complexity : O(n) because we simply traverse the given string one 
# character at a time and push and pop operations on a stack take O(1) time.
# Space complexity : O(n) as we push all opening brackets onto the stack and 
# in the worst case, we will end up pushing all the brackets onto the stack.

class Solution:
    def isValid(self, s: str) -> bool:
        if s == "": 
            return True
        
        bracket_mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for bracket in s:
            if bracket not in bracket_mapping:
                stack.append(bracket)
            elif bracket_mapping[bracket] in stack: 
                stack.pop()
            else: 
                return False
        
        # If the stack is empty we have closed all brackets correctly 
        if not stack: 
            return True 
        # If the stack is not empty after finishing, the brackets did not 
        # close in the correct order
        return False
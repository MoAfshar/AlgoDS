"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
    Input: A = 'abcde', B = 'cdeab'
    Output: true

Example 2:
    Input: A = 'abcde', B = 'abced'
    Output: false
    
Note:
A and B will have length at most 100.
"""
class Solution:
    # Time Complexity is O(N) "in" operator is linear in lists
    # Space Complexity is O(N) because of additional A in A+A
    def rotateString(self, A: str, B: str) -> bool: 
        if len(A) != len(B): 
            return False
        # All rotation s of A are contained in A+A  
        if B in A+A: 
            return True 
        return False
    
    # Time Complexity: O(N^2), where N is the length of A. For each rotation s, we check up to N elements in A and B.
    # Space Complexity: O(1)
    def rotateString2(self, A: str, B: str) -> bool:
        if len(A) != len(B): 
            return False 
        if A == B or len(A) == 0: 
            return True 
        print(A+A)
        
        A, B = list(A), list(B)
        for i in range(len(A)): 
            self.rotate(A)
            if A == B: 
                return True 
        return False
    
    def rotate(self, A: List[str]): 
        previous = A[0]
        A[0] = A[-1]
        for i in range(1, len(A)): 
            tmp = A[i]
            A[i] = previous 
            previous = tmp
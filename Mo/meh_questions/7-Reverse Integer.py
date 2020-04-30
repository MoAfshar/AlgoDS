"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output: 321
    
Example 2:

    Input: -123
    Output: -321
    
Example 3:

    Input: 120
    Output: 21
    
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0: 
            x = x * -1
            negative = True
            
        reverse = 0
        while x > 0:
            last_digit = x % 10 # Isolate the final number 
            reverse = (reverse * 10) + last_digit # Append the last digit to reverse
            x = x // 10 # remove last digit from number
        
        if reverse >= (2 ** 31) - 1: 
            return 0
        if negative: 
            return reverse * -1
        return reverse
    
    def reverse2(self, x: int) -> int:
        if x >= (2 ** 31) - 1 or x <= (-2 ** 31): 
            return 0
        
        elif x >= 0: 
            x = list(str(x))
            x = self.reverseString(x)
            x = int(''.join(x))
        else: 
            x = list(str(x)) 
            x = self.reverseString(x[1:])
            x.insert(0, '-')
            x = int(''.join(x))
        
        if x >= (2 ** 31) - 1 or x <= (-2 ** 31): 
            return 0
        return x
    
    def reverseString(self, s: List[str]) -> List[str]:
        start = 0
        end = len(s) - 1
        while start < end: 
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp 
            start += 1
            end -= 1
        return s
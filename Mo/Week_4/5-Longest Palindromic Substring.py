"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    
Example 2:

    Input: "cbbd"
    Output: "bb"
"""
# The idea is to expand out from every character towards the left and the right side of the string
# This is because a palindrome would be the same if we are expanding from the centre 
# We will have two cases (odd and eve) e.g aba or abba -> we will have to cover both cases 
# Time complexity will be O(n^2) and space complexity will be O(N)
class Solution: 
    def longestPalindrome(self, s: str) -> str:  
        if not s or len(s) == 1: 
            return s
        
        result = ""
        for i in range(0, len(s)): 
            # For the case where the length is odd
            pali1 = self.expandFromCentre(s, i, i)
            # For the case where the length is even
            pali2 = self.expandFromCentre(s, i, i+1) 
            # Check whether the new palindrome is bigger than the previous one
            if len(pali1) > len(result): 
                result = pali1
            if len(pali2) > len(result):
                result = pali2
        return result
                
    # This will give us the longest possible palindrome we can achieve based on our iterations 
    # The minimum will always be 1 and the maximum can be length of the whole string
    # Get the longest string from 
    def expandFromCentre(self, s: str, left: str, right: str) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]: 
            left -= 1
            right += 1
        return s[left+1:right]

# Brute Force Solution - Loop through every possibility and store the results in a list and return the max 
# O(n^3) time compelxity and O(N) space complexity
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return ""
        
        s = list(s)
        final_subs = []
        for i in range(0, len(s)):
            curr = ""
            for j in range(i, len(s)): 
                curr += s[j]
                if self.isPalindrome(curr): 
                    final_subs.append(curr)
        return max(final_subs, key=len)
    
    def isPalindrome(self, s: str) -> bool: 
        s = list(s)
        start = 0
        end = len(s) - 1
        while start < end: 
            if s[start] != s[end]:
                return False 
            start += 1
            end -= 1
        return True
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 
    
Example 2:

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    
Example 3:

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. 
                 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution: 
    # Using the sliding window approach O(2n) = O(N)
    def lengthOfLongestSubstring(self, s: str) -> int: 
        pointer_a, pointer_b = 0, 0
        s = list(s)
        visited = {}
        max_subarray = 0
        while pointer_b < len(s): 
            if s[pointer_b] not in visited:
                visited[s[pointer_b]] = 1 
                max_subarray = max(len(visited), max_subarray)
                pointer_b += 1
            else: 
                del visited[s[pointer_a]]
                pointer_a += 1
        return max_subarray

# Brute force solution
# Time complexity: O(n^3) 
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        global_max = 0
        for i in range(0, len(s)): 
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                # Check for each substring whether the string is unique, if so update maximum value
                if self.isUnique(curr): 
                    global_max = max(global_max, j-i+1)
        return global_max
    
    def isUnique(self, s: str) -> bool: 
        visited = {}
        for char in s: 
            if char in visited: 
                return False
            else: 
                visited[char] = 1
        return True
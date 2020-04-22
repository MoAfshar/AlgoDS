"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true
    
Example 2:

    Input:pattern = "abba", str = "dog cat cat fish"
    Output: false
    
Example 3:

    Input: pattern = "aaaa", str = "dog cat cat dog"
    Output: false
    
Example 4:

    Input: pattern = "abba", str = "dog dog dog dog"
    Output: false
    
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, strs: str) -> bool:
        pattern_map = {}
        strs_list = strs.split(' ')
        if len(pattern) != len(strs_list): 
            return False
        
        for i in range(len(pattern)): 
            char = pattern[i] 
            word = strs_list[i]
            if char not in pattern_map and word not in pattern_map.values(): 
                pattern_map[char] = word
            elif char not in pattern_map or pattern_map[char] != word:
                return False 
        return True
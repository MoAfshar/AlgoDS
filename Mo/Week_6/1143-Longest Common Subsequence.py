"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
 
Example 1:

	Input: text1 = "abcde", text2 = "ace" 
	Output: 3  
	Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

	Input: text1 = "abc", text2 = "abc"
	Output: 3
	Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

	Input: text1 = "abc", text2 = "def"
	Output: 0
	Explanation: There is no such common subsequence, so the result is 0. 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""

# Great video for algorithm https://www.youtube.com/watch?v=ASoaQq66foQ
# The time complexity is O(n*m) and Space compelxity is O(n*m) 
# where n = len(str1) and m = len(str2)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Make a 2d table - plus 1 to include the empty string
        text1 = " " + text1
        text2 = " " + text2
        cols = len(text1)
        rows = len(text2)
        dp_table = [[None for x in range(cols)] for y in range(rows)]
        
        # Initialise the first row and first column to be zero 
        # This is because when we reduce the problem to a subsequence and empty string 
        # It will always be 0 
        for i in range(cols):
            dp_table[0][i] = 0
            
        for i in range(rows): 
            dp_table[i][0] = 0
        
        for i in range(1, rows): # row
            for j in range(1, cols): # column
                if text1[j] == text2[i]: 
                    dp_table[i][j] = 1 + dp_table[i-1][j-1]
                else: 
                    dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])
        
        return dp_table[rows-1][cols-1]

# Cleaner version 
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cols = len(text1)
        rows = len(text2)
        dp_table = [[0 for x in range(cols+1)] for y in range(rows+1)]
        
        for i in range(rows):
            for j in range(cols): 
                if text1[j] == text2[i]: 
                    dp_table[i+1][j+1] = 1 + dp_table[i][j]
                else: 
                    dp_table[i+1][j+1] = max(dp_table[i][j+1], dp_table[i+1][j])
        
        return dp_table[-1][-1]
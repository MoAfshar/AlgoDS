"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

    Input: m = 3, n = 2
    Output: 3
    
Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right
    
Example 2:

    Input: m = 7, n = 3
    Output: 28
"""
# Essentially we want to check how many different ways we can reach each cell 
# We can only reach the first column and first row once since we can only move right or down
# we will first fill out our dp grid for first column and row. 
# Than for each cell we calculate how many unique times we can reach it 
# For each cell we could have came either from its left or top. Adding the the unique 
# ways from pervious cells will gives the ways for the current cell and we continue
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # n=rows, m=cols - Initialise a dp grid with all 0's grid[row][column]
        grid = [[0 for x in range(m)] for y in range(n)] # create column first than row
        
        for i in range(m):
            grid[0][i] = 1
            
        for i in range(n):  
            grid[i][0] = 1
            
        # For any cell we come we can either come from above or from the left
        for i in range(1, n): # For each column - we can start from 1 since we filled out
            for j in range(1, m): # For each row - we can start from 1 since we filled out
                grid[i][j] = grid[i][j-1] + grid[i-1][j]
                    
        return grid[n-1][m-1]
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    
Example 2:

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""

# The way to think about dynamic programming is to have a bottom up approach 
# Think of the initial base cases that are required to solve the problem, after solving the base cases
# think of the next simple case, and see whether that can be used by combining the previous sub problems 
# Also this problem is pretty much fibonnaci - you get the same sequence :)
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp will hold a list of all the ways we can climb the stairs 
        # The first two base cases are at 0 steps and 1 steps there are only 1 way to climb the steps 
        dp = [1, 1]
        #loop through 2 stair cases up to n
        for i in range(2, n+1):
            # We can only take 2 steps at most, we had to come from the step before it or 2 steps before it
            # Getting to the i'th step - the only way is to get to the previous step or 2 steps before it 
            # And we have already solved those sub problems
            dp.append(dp[i-1] + dp[i-2])
        
        return dp[n]
            
        
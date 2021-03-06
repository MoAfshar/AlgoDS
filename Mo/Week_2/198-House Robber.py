"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.
                 
Example 2:

    Input: [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                 Total amount you can rob = 2 + 9 + 1 = 12.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        
        # Create a DP array which will hold the maximum amount of money which we can rob until that house
        dp = [0] * n
        # Maximum money stolen from 1 house
        dp[0] = nums[0]
        # Maximum money stolen from 2 houses
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)): 
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
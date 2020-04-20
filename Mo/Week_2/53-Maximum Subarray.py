"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
"""
class Solution:
    # Kadane's algorithm O(n)
    # Using the values of the maximum's found of the previous index, we can use DP to solve this
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        for i in range(1, len(nums)): 
            # Calculate the maximum sub-array - either the number it self or the addition with previous
            max_current = max(nums[i], nums[i] + max_current)
            if max_current > max_global: 
                max_global = max_current
        return max_global
    
    # O(N^2) solution - Brute Force
    def maxSubArray2(self, nums: List[int]) -> int: 
        max_current = float('-inf')
        for i in range(0, len(nums)): 
            current = 0
            for j in range(i, len(nums)): 
                current += nums[j]
                max_current = max(current, max_current)
        return max_current
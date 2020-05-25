"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

    Input: [10,9,2,5,3,7,101,18]
    Output: 4 
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

# Time complexity is O(n^2) and Space complexity is O(n)
# Idea is to use DP, using previous sub-problems to helps us reach the global maximum
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        result = [1] * len(nums)
        
        for i in range(1, len(nums)): 
            j = 0 
            while j != i:
                if nums[i] > nums[j]: 
                    new_val = 1 + result[j]
                    result[i] = max(new_val, result[i])
                j += 1 
                
        return max(result)
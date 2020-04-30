"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

    Input: [1,3,5,6], 5
    Output: 2
    
Example 2:

    Input: [1,3,5,6], 2
    Output: 1
    
Example 3:

    Input: [1,3,5,6], 7
    Output: 4
    
Example 4:

    Input: [1,3,5,6], 0
    Output: 0
"""
class Solution:
    # Time complexity is O(N) and space complexity is O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)): 
            if target < nums[i] or target == nums[i]: 
                return i 
        return len(nums)
    
    # Time complexity is O(logn) and space complexity is O(1)
    def searchInsert(self, nums: List[int], target: int) -> int: 
        left = 0
        right = len(nums) - 1
        while left <= right: 
            middle = (left + right) // 2
            if target == nums[middle]: 
                return middle 
            elif target > nums[middle]: 
                left = middle + 1
            else: 
                right = middle - 1
        return left
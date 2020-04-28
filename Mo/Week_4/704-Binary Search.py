"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
 

Note:
You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""
# For binary search we need to pointers starting at the end and start of our list
# We find the middle point by adding left + right // 2
# If the value we find is the target then simply return the index 
# If the value we find is larger than our target -> move the right pointer to middle - 1 
# If the value we fins is smaller than our target -> move the left pointer to middle + 1
# Time complexity is O(logn) and space complexity is O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right: 
            middle = (left + right) // 2
            if nums[middle] == target: 
                return middle
            if nums[middle] > target: 
                right = middle - 1
            elif nums[middle] < target: 
                left = middle + 1
        return -1 
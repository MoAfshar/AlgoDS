"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

    Input: [3,4,5,1,2] 
    Output: 1
    Example 2:

    Input: [4,5,6,7,0,1,2]
    Output: 0
"""
# Since the array is sorted we can perform a modified binary search to find the minimum 
# number in the array. Assuming no duplicates
# Time complexity O(logn), Space complexity is O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right: 
            middle = (left + right) // 2
            if nums[middle] > nums[right]: 
                left = middle + 1
            else: 
                right = middle 
        return nums[left]
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    
Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
"""

# A better solution would be to use binary search to find the pivot point
# Then check based on the pivot points value and the end values whether we need to search the first part of 
# the string or the second part 
# Once determining which part of the string we need to search we can simply run binary search on it
class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        if not nums: 
            return -1 
        
        pivot = self.findPivot(nums)
        left = 0
        right = len(nums) - 1
        # Find the boundary of the binary search, so we only search one side
        if nums[pivot] <= target and nums[-1] >= target: 
            left = pivot
        else: 
            right = pivot - 1
        return self.binarySearch(nums, target, left, right)
        
    # Use binary search to find the pivot
    def findPivot(self, nums: List[int]) -> int: 
        left = 0
        right = len(nums) - 1
        # our goal is for these indexes to meet each other at the pivot point 
        # e.g if left = right we want to quit the loop 
        while left < right: 
            middle = (right + left) // 2
            # if the middle number is greater than the final number of the array
            # we move ourleft pointer to middle + 1 to narrow our search in finding the smallest value
            if nums[middle] > nums[right]: 
                left = middle + 1
            else: 
                right = middle
        return left
                
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int: 
        while left <= right: 
            middle = (left + right) // 2
            if nums[middle] == target: 
                return middle 
            elif nums[middle] > target: 
                right = middle - 1
            elif nums[middle] < target: 
                left = middle + 1
        return -1

# First intuitive solution uses O(N) and O(1) space (kinda dumb if O(N) then just traverse list and find it)
# Find the pivot moment, by doing so we wil then have two sorted list 
# Perform binary search on the correct boundary to return result
class Solution2: 
    def search(self, nums: List[int], target: int) -> int:
        if not nums: 
            return -1 
        
        k = self.findPivot(nums)
        left = 0 
        right = len(nums) - 1
        if nums[k] <= target and nums[right] >= target: 
            left = k
        else: 
            right = k - 1
        return self.binarySearch(nums, target, left, right)
    
    def findPivot(self, nums: List[int]) -> int: 
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]: 
                return i + 1
        return 0
    
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int: 
        while left <= right: 
            middle = (left + right) // 2
            if nums[middle] == target: 
                return middle 
            elif nums[middle] > target: 
                right = middle - 1 
            elif nums[middle] < target: 
                left = middle + 1
        return -1
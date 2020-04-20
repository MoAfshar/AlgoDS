"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    
Note: You must do this in-place without making a copy of the array. 
      Minimize the total number of operations.
"""
class Solution:
    # The idea is to keep a tracker in place for the index. 
    # Everytime we encounter a number that is not 0, start by appending it to the beginning of 
    # the list - and incrementing the index by 1. 
    # By doing so we will append all of the none-zero numbers to the beginning of the list
    # without changing their order 
    # Finally since we have kept track of the index we can fill the rest by 0's by only
    # looping from the index -> length of the list
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0: 
                nums[index] = nums[i]
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0
    
    # Brute force really bad - first thing coming to my mind
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)-1): 
            for j in range(0, len(nums)-1): 
                if nums[j] == 0: 
                    tmp = nums[j+1] 
                    nums[j+1] = nums[j]
                    nums[j] = tmp
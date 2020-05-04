"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
"""
# When thinking about the problem it is important to think about whether there are going to be any duplicates
# whether there all numbers are unique or not etc to scope out the problem for ourselves
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        result = []
        nums.sort() # Sorts in place
        target = 0
        for i in range(0, len(nums)-2):
            # for the case where all numbers are all the same in the list e.g [0, 0, 0]
            if i == 0 or nums[i] != nums[i-1]:
                start = i + 1
                end = len(nums) - 1
                while start < end: 
                    if nums[i] + nums[start] + nums[end] == target: 
                        result.append([nums[i], nums[start], nums[end]])
                    if nums[i] + nums[start] + nums[end] < target: 
                        # Increment the left pointer and avoid duplication with the while loop
                        # If the next element is the same as our current increase pointer again
                        # Always executes at least once
                        current_start = start
                        while nums[current_start] == nums[start] and start < end: 
                            start += 1
                    else: 
                        # Increment the right pointer and avoid duplication with the while loop
                        # If the next element is the same as our current increase pointer again
                        # Always executes at least once
                        current_end = end
                        while nums[current_end] == nums[end] and start < end: 
                            end -= 1
        return result
    
    # Brute Force O(n^3)
    # Find all the combinations - store in a tuple if the addition equals the target 
    # Apply set to the tupple to get rid of duplicates and convert back to list and return 
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        target = 0
        print(nums)
        for i in range(0, len(nums)-2): 
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)): 
                    if nums[i] + nums[j] + nums[k] == target: 
                        result.append((nums[i], nums[j], nums[k]))
        return list(set(result)) # O(N) time complexity
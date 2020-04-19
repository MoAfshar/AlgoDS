"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    
Example 2:

    Input: [-1,-100,3,99] and k = 2
    Output: [3,99,-1,-100]
    Explanation: 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
    
Note: Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem. Could you do it in-place with O(1) extra space?
"""
# Had to look at solution for both approaches 
class Solution:
    # The trick is to: 
    # 1 - reverse the list 
    # 2 - reverse the first k number of the reversed list 
    # 3 - reverse the rest of the list
    # Create a reverse function that will reverse based on the index you give it
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Simple reverse algorithm, swap the ends of the list
        def reverse(nums, start, end): 
            while start < end: 
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start += 1
                end -= 1
                
        # For when length of k <= len(k)
        k = k % len(nums)
        # reverse the list
        reverse(nums, 0, len(nums)-1)
        # reverse the first k number of the reversed list
        reverse(nums, 0, k-1)
        # reverse the rest of the list
        reverse(nums, k, len(nums)-1)                
    
    # Brute force solution 
    def rotate2(self, nums: List[int], k: int) -> None: 
        for i in range(k): 
            previous = nums[-1]
            # Perform a swap from end to front and continue k times 
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
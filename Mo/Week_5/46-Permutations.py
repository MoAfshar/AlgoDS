"""
Given a collection of distinct integers, return all possible permutations.

Example:

    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
"""
# Time complexity O(n!) since there are no duplicates 
# This is a bit better using dictionary for O(1) insertion and pop()
class Solution: 
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] # Will hold our final permutation list 
        temp = {} # This will hold the intermediate result 
        self.backTrack(result, temp, nums)
        return result
    
    def backTrack(self, result, temp, nums): 
        if len(temp) == len(nums): 
            temp_copy = temp.copy()
            result.append(temp_copy)
        else: 
            for i in range(len(nums)): 
                if nums[i] not in temp: 
                    temp[nums[i]] = None
                    self.backTrack(result, temp, nums)
                    del temp[nums[i]]

# Try to implement this backtracking with a set/hashmap instead of a temp list again
# Time complexity is O(n!) 
class Solution2:
    def backTrack(self, nums, result, temp):
        if len(temp) == len(nums):
            # Since the algorithm performs tempList.remove(tempList.size() - 1) at the end 
            # of every iteration, we will end up with an empty tempList at the end of 
            # the method thus final result shows that list contains the entries all pointing 
            # to the same empty tempList. So a copy is needed 
            # Since we modify temp - the final list in result also changes
            temp = temp.copy() 
            result.append(temp)
        else: 
            for i in range(len(nums)):
                if nums[i] not in temp: 
                    temp.append(nums[i])
                    self.backTrack(nums, result, temp)
                    temp.pop()
                else: 
                    continue
                    
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        self.backTrack(nums, result, temp)
        return result 
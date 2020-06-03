"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
class Solution:
    # Check the solutions page for more details - no idea how they came up with this algorithm
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        L, R = [0] * len(nums), [0] * len(nums)
        result = []
        
        L[0] = 1
        for i in range(1, len(nums)): 
            L[i] = nums[i-1] * L[i-1]
        
        R[-1] = 1
        for i in reversed(range(len(nums)-1)): 
            R[i] = nums[i+1] * R[i+1]
            
        for i in range(len(nums)): 
            result.append(L[i] * R[i])
        
        return result
    
    # We can simply take the product of all the elements in the given array and then, for 
    # each of the elements x of the array, we can simply find product of array except
    # self value by dividing the product by x.
    def productExceptSelf2(self, nums: List[int]) -> List[int]: 
        product, zeros = self.calcProduct(nums) 
        result = []
        for i in nums: 
            if zeros == 0: 
                result.append(product // i)
            elif zeros == 1 and i == 0: 
                result.append(product)
            else: 
                result.append(0)
        return result
    
    # First thought of the solution 
    # Time complexity is O(N^2) and space complexity of O(N) if the output array is not considered as extra space
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        previous = []
        result = []
        for i in range(len(nums)): 
            result.append(self.calcProduct(nums[i+1:]) * self.calcProduct(previous))
            previous.append(nums[i])
        
        return result
    
    def calcProduct(self, nums: List[int]) -> int: 
        product = 1
        zeros = 0
        for i in range(len(nums)): 
            if nums[i] == 0: 
                zeros += 1
            else: 
                product *= nums[i]
            
        return product, zeros
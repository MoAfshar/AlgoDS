# Description 
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

    Input: [2,2,1]
    Output: 1
    
Example 2:

    Input: [4,1,2,1,2]
    Output: 4
"""


# Bitmanipulation explanation
"""
Example for [2,1,4,5,2,4,1] - using XOR and since its commutative and A XOR A = 0
=> 0 ^ 2 ^ 1 ^ 4 ^ 5 ^ 2 ^ 4 ^ 1

=> 0^ 2^2 ^ 1^1 ^ 4^4 ^5 (Rearranging, taking same numbers together)

=> 0 ^ 0 ^ 0 ^ 0 ^ 5

=> 0 ^ 5

=> 5 :)
"""
class Solution: 
    def singleNumber(self, nums: List[int]) -> int: 
        a = 0
        for i in nums: 
            a = a ^ i
        return a

# Math solution no idea how to come up with it
class Solution2: 
    def singleNumber(self, nums: List[int]) -> int: 
        return 2 * sum(set(nums)) - sum(nums)

# Store in hashmap and then iterate through hashmap to get the one with value 1
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        visited = {}
        for i in nums: 
            if i not in visited:
                visited[i] = 1
            else: 
                visited[i] += 1
                
        for key, value in visited.items(): 
            if value == 1: 
                return key
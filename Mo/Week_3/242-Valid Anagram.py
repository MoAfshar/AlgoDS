"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:

    Input: s = "rat", t = "car"
    Output: false
    
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    # Time complexity: O(n) because accessing the counter table is constant time operation.
    # Space complexity: O(1). Although we do use extra space, the space complexity is O(1) because the table's 
    # size stays constant no matter how large nn is.
    
    # Use 1 hashmap instead, store the first string in the hashmap 
    # iterate through the second string and if it exists in hashmap decrease total 
    # For an exact match the final values should all be 0's otherwise mismatch
    def isAnagram(self, s: str, t:str) -> bool: 
        if len(s) != len(t): 
            return False 
        
        table_count = {}
        for char in s: 
            if char not in table_count: table_count[char] = 1
            else: table_count[char] += 1 
        
        for char in t: 
            if char not in table_count: return False 
            elif char in table_count: table_count[char] -= 1
            if table_count[char] < 0: return False # If any values decreases < 0 we can instantly return False
            
        return True # All values match exactly and there is no difference
        
        # Instead of checking the values < 0 - we can also check whether all values are 0 or not
        # for count in table_count.values(): 
        #     if count != 0: 
        #         return False 
        # return True
    
    # Using 2 hashmaps - two counter tables to compare whether the count of each occurences of each letter in 
    # the two string are the same - if so we can return true 
    # Time complexity: O(n) because accessing the counter table is constant time operation.
    # Space complexity: O(1). Although we do use extra space, the space complexity is O(1) because the table's 
    # size stays constant no matter how large N is.
    def isAnagram2(self, s: str, t:str) -> bool: 
        map1, map2 = {}, {}
        for i in s: 
            if i not in map1: map1[i] = 1
            else: map1[i] += 1
        for i in t: 
            if i not in map2: map2[i] = 1
            else: map2[i] += 1
                
        return map1 == map2
        
    # Dumb method because python lol
    # Running time is O(NlogN)
    # Space complexity, sorted uses timsort which at worst case is O(N) or at best case O(1)
    def isAnagram3(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
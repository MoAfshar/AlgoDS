"""
Given an array of strings, group anagrams together.

Example:

    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    
Note:
- All inputs will be in lowercase.
- The order of your output does not matter.
"""
# Two strings are anagrams if and only if their sorted strings are equal.
# Unsure about how to calculate the time complexity
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}           
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in answer: 
                answer[sorted_word] = [word]
            else: 
                answer[sorted_word].append(word)
        return answer.values()
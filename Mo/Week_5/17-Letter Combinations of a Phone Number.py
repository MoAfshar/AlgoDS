"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

Example:

    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
# We try a BFS kind of solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        result = ""
        deq = deque([result])
        for i in range(len(digits)): # We iterate through each digit
            index = digits[i] 
            for j in range(len(deq)): # For each element in the queue 
                perm = deq.popleft()  # get that element
                for k in range(len(phone[index])):  # add the coresponding values to each element
                    deq.append(perm + phone[index][k])
        return deq
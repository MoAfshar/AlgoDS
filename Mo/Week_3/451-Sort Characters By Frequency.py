"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

    Input:
    "tree"

    Output:
    "eert"

    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

    Input:
    "cccaaa"

    Output:
    "cccaaa"

    Explanation:
    Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
    Note that "cacaca" is incorrect, as the same characters must be together.
    
Example 3:

    Input:
    "Aabb"

    Output:
    "bbAa"

    Explanation:
    "bbaA" is also a valid answer, but "Aabb" is incorrect.
    
Note that 'A' and 'a' are treated as two different characters.
"""
class Solution:
    # Using a hashmap and a bucket strategy O(N) time
    def frequencySort(self, s: str) -> str: 
        frequency = {}
        # Store all the characters and their frequency 
        for char in s: 
            if char not in frequency: 
                frequency[char] = 1 
            else: 
                frequency[char] += 1
        
        # Store each element in a bucket based on their occurance 
        # Index of bucket = occurance of word
        bucket = [None] * (len(s) + 1)
        for k, v in frequency.items(): 
            if bucket[v] == None: 
                bucket[v] = [k]
            else: 
                bucket[v].append(k)
                
        # Loop through the bucket from the end, and join/append the occurances to the final string
        sorted_char_frequency = ""
        for i in range(len(bucket)-1, -1, -1): 
            if bucket[i] != None: 
                for j in bucket[i]: 
                    sorted_char_frequency += str(j) * i
                
        return sorted_char_frequency
            
    # Using a hashmap first to store the frequency 
    # Then sorting it and printing the string per frequency 
    # Runtime is O(NlogN)- Most intuitive way to first think about this question
    def frequencySort2(self, s: str) -> str:
        frequency = {}
        for char in s: 
            if char not in frequency: 
                frequency[char] = 1 
            else: 
                frequency[char] += 1
                
        sorted_chars = ""
        sorted_frequencies = sorted(frequency, key=frequency.get, reverse=True)
        for k in sorted_frequencies:
                sorted_chars += k * frequency[k]
        return sorted_chars
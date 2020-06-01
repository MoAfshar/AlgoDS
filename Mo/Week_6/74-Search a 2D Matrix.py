"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    Output: true
    
Example 2:

    Input:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 13
    Output: false
"""
class Solution:
    # We need to use the special property of the list where each list is ordered i.e
    # The first integer of each row is greater than the last integer of the previous row.
    # The by doing binary search we can get:
    #   - Time Complexity O(log(N*M)) and Space Complexity of O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        if not matrix or target is None: 
            return False 
        
        rows, cols = len(matrix), len(matrix[0])
        left = 0 
        right = rows * cols - 1
        while left <= right: 
            middle = (left + right) // 2
            # middle // cols gives the row 
            # middle % cols gives the column
            if matrix[middle // cols][middle % cols] == target: 
                return True 
            elif matrix[middle // cols][middle % cols] < target:  
                left = middle + 1
            else: 
                right = middle - 1
        return False    
    
    # This solution has time complexity of O(Nlog(M)) and space complexity of O(1)
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool: 
        if not matrix or target is None: 
            return False 
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, cols - 1
        for i in range(rows):
            if self.binarySearch(matrix[i], left, right, target): 
                return True 
        return False
    
    def binarySearch(self, board: List[int], left: int, right: int, target: int) -> bool: 
        while left <= right: 
            middle = (left + right) // 2
            if board[middle] == target: 
                return True
            elif board[middle] < target: 
                left = middle + 1
            else: 
                right = middle - 1
        return False
    
    # Brute force, Time Complexity O(MxN) and Space complexity O(1)
    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None: 
            return False
        
        rows, cols = len(matrix), len(matrix[0])
                
        for i in range(rows):
            for j in range(cols): 
                if matrix[i][j] == target: 
                    return True 
        return False
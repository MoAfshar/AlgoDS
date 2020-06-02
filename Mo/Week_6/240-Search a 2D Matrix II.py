"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:

    Consider the following matrix:

    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    Given target = 5, return true.

    Given target = 20, return false.
"""
class Solution:
    # Best solution would be of Time complexity of O(M+N) and Space complexitry O(1) 
    # initialize the current position to top right corner, if the target is greater than the 
    # value in current position, then the target can not be in entire row of current position
    # because the row is sorted, if the target is less than the value in current position, 
    # then the target can not in the entire column because the column is sorted too. 
    # We can rule out one row or one column each time, so the time complexity is O(m+n).
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        if not matrix or target is None: 
            return False 
        
        rows = 0
        cols = len(matrix[0]) - 1
        while rows <= len(matrix)-1 and cols >= 0: 
            if matrix[rows][cols] == target:
                return True 
            elif matrix[rows][cols] > target: 
                cols -= 1
            elif matrix[rows][cols] < target: 
                rows += 1
                
        return False 
    
    # Second solution that comes to mind is to perform binary search per each row 
    # Since each row is sorted 
    # Time complexity of O(N*log(M)) and Space complexity of O(1)
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool: 
        if not matrix or target is None: 
            return False 
        
        rows, cols = len(matrix), len(matrix[0])
        left = 0
        right = cols - 1
        for i in range(rows): 
            if self.binarySearch(matrix[i], left, right, target): 
                return True 
        return False 
    
    def binarySearch(self, row: List[int], left: int, right: int, target: int) -> bool: 
        while left <= right: 
            middle = (left + right) // 2
            if row[middle] == target: 
                return True 
            elif row[middle] < target: 
                left = middle + 1
            else: 
                right = middle - 1
        return False
    
    # Using brute force Time complexity is O(M*N) and Space complexity of O(1)
    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None: 
            return False 
        
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows): 
            for j in range(cols): 
                if matrix[i][j] == target: 
                    return True 
        return False
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

    Input:
    11110
    11010
    11000
    00000

    Output: 1
    Example 2:

    Input:
    11000
    11000
    00100
    00011

    Output: 3
"""
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0 
        if not grid: 
            return 0
        
        land = '1'
        water = '0'
        # Rows 
        for i in range(len(grid)):
            # Columns
            for j in range(len(grid[i])):
                if grid[i][j] == land: 
                    # when we find an island -> check the surrounding and change the state 
                    # So we do not visit the same island again 
                    # This dfs call's purpose is to just change the state of our current grid
                    number_of_islands += self.dfs(grid, i, j)
                    
        return number_of_islands
    
    def dfs(self, grid: List[List[str]], i: int, j: int) -> int:
        # Boundary Check 
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0': 
            return 0 
        
        # Otherwise turn the land into water and check neighbours recursively 
        grid[i][j] = '0'
        self.dfs(grid, i, j+1) # Right
        self.dfs(grid, i, j-1) # Left
        self.dfs(grid, i+1, j) # Down
        self.dfs(grid, i-1, j) # Up
        return 1
    
class Solution: 
    def BFS(self, grid: List[List[str]], visited: List[List[bool]], deq: deque) -> None: 
        while deq: 
            i, j = deq.popleft()
            if i < 0 or i >= len(grid)  or j < 0 or j >= len(grid[i]) or visited[i][j]or grid[i][j] != '1':
                continue

            visited[i][j] = True
            deq.append((i, j+1)) 
            deq.append((i, j-1))
            deq.append((i+1, j))
            deq.append((i-1, j))
                
    def numIslands(self, grid: List[List[str]]) -> int: 
        number_of_islands = 0
        land = '1'
        # visited = grid - NOTE TO SELF DO NOT DO THIS - This only makes a refrence copy
        from copy import deepcopy
        visited = deepcopy(grid)
        for i in range(len(visited)): 
            for j in range(len(visited[i])): 
                visited[i][j] = False 
        
        deq = deque([])
        for i in range(len(grid)): 
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == land: 
                    deq.append((i, j))
                    self.BFS(grid, visited, deq)
                    number_of_islands += 1
                    
        return number_of_islands
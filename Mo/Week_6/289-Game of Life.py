"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

    Input: 
    [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    Output: 
    [
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]
    ]
    
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.

In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
# Time Complexity: O(M×N), where M is the number of rows and N is the number of columns of the Board.
# Space Complexity: O(1)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None: 
        rows, cols = len(board), len(board[0])
        for i in range(0, rows): 
            for j in range(0, cols): 
                neighbours = self.getNeighbours(board, i, j)
                live_neighbours = 0
                for neighbour in neighbours: 
                    if neighbour % 2 != 0: #it's odd so it has been alive 
                        live_neighbours += 1
                # We can use the following encoding 
                # dead -> dead = 0 - we do not need to take care of it
                # alive -> dead = 1
                if board[i][j] % 2 != 0 and (live_neighbours < 2 or live_neighbours > 3): 
                    board[i][j] = 1
                # dead -> alive = 2
                elif board[i][j] % 2 == 0 and live_neighbours == 3: 
                    board[i][j] = 2
                # alive -> alive = 3
                elif board[i][j] % 2 != 0: 
                    board[i][j] = 3
                
        # final loop to fix the labels accordingly 
        for i in range(0, rows): 
            for j in range(0, cols): 
                if board[i][j] == 2 or board[i][j] == 3: 
                    board[i][j] = 1
                else: 
                    board[i][j] = 0
                    
    
# Time Complexity: O(M * N)O(M×N), where M is the number of rows and N is the number of columns of the Board.
# Space Complexity: O(M * N)O(M×N), where M is the number of rows and NNis the number of columns of the Board. This is the space occupied by the copy board we created initially.
    def gameOfLife2(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = deepcopy(board)
        
        for i in range(0, len(board_copy)): 
            for j in range(0, len(board_copy[0])):
                neighbours = self.getNeighbours(board_copy, i, j)
                live_neighbours = 0
                for neighbour in neighbours: 
                    if neighbour == 1: 
                        live_neighbours += 1
                if board_copy[i][j] == 1 and (live_neighbours < 2 or live_neighbours > 3): 
                    board[i][j] = 0 
                elif board_copy[i][j] == 0 and live_neighbours == 3: 
                    board[i][j] = 1 
                
    def getNeighbours(self, board: List[List[int]], i: int, j: int) -> List[int]:
        neighbours = []
        rows, cols = len(board), len(board[0])
        if i > 0: neighbours.append(board[i-1][j])
        if j > 0: neighbours.append(board[i][j-1])
        if i < rows-1: neighbours.append(board[i+1][j])
        if j < cols-1: neighbours.append(board[i][j+1])
        # Diags 
        if i > 0 and j > 0: neighbours.append(board[i-1][j-1])
        if i > 0 and j < cols-1: neighbours.append(board[i-1][j+1])
        if i < rows-1 and j > 0: neighbours.append(board[i+1][j-1])
        if i < rows-1 and j < cols-1: neighbours.append(board[i+1][j+1])
        
        return neighbours
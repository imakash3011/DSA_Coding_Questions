'''https://leetcode.com/problems/n-queens/'''


from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        # Represent the board as a list of strings
        board = ["." * n for _ in range(n)]
        
        def safe_or_not(row, col, board, n):
            # 1. Check this row on the left side
            for i in range(col):
                if board[row][i] == 'Q':
                    return False
            
            # 2. Check upper diagonal on the left side
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
                
            # 3. Check lower diagonal on the left side
            i, j = row, col
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1
                
            return True

        def helper_func(col, board, n):
            # Base Case: If all queens are placed, save the current board state
            if col == n:
                result.append(list(board))
                return
            
            # Try placing a queen in each row for the current column
            for row in range(n):
                if safe_or_not(row, col, board, n):
                    # Place the Queen
                    board[row] = board[row][:col] + "Q" + board[row][col+1:]
                    
                    # Recur to place the rest of the queens
                    helper_func(col + 1, board, n)
                    
                    # Backtrack: Remove the Queen
                    board[row] = board[row][:col] + "." + board[row][col+1:]
        
        # Start the recursive process from the 0-th column
        helper_func(0, board, n)
        return result



n = 4
c1= Solution()
print(c1.solveNQueens(n))
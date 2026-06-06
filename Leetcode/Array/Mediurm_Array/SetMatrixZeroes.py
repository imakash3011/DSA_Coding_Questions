'''
https://leetcode.com/problems/set-matrix-zeroes/
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_lst = []
        col_lst = []

        row_n = len(matrix)
        col_n = len(matrix[0])
        print(row_n, col_n)
        for row in range(row_n):
            for col in range(col_n):
                if matrix[row][col] == 0:
                    row_lst.append(row)
                    col_lst.append(col)
        print(row_lst, col_lst)
        for row in range(row_n):
            for col in range(col_n):
                if row in row_lst:
                    matrix[row][col]=0
                if col in col_lst:
                    matrix[row][col]=0
        return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
c1 = Solution()
print(c1.setZeroes(matrix))
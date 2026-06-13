'''
https://leetcode.com/problems/rotate-image/description/
'''

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         row = len(matrix)
#         col = len(matrix[0])

#         new_matrix = [[0 for _ in range(col)] for _ in range(row)]
#         temp = col-1
#         for i in range(row):
#             for j in range(col):
#                 new_matrix[j][temp] = matrix[i][j]
#             temp -=1
#         matrix[:] = [row[:] for row in new_matrix]
#         return matrix


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        ## Transpose Matrix
        for i in range(row):
            for j in range(i+1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        ## Reverse row (row which is required at end will come first that's why reverse is required)
        for k in range(row):
            matrix[k].reverse() # think matrix list of list.. here we are taking one list at a time and we reversing its number
        
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
c1 = Solution()
print(c1.rotate(matrix))
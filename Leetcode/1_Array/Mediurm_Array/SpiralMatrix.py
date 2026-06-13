'''
https://leetcode.com/problems/spiral-matrix/description/
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        row = len(matrix)
        col = len(matrix[0])

        left, top = 0,0
        right, bottom = col-1, row-1

        new_res = []
        # for left to right
        while top<= bottom and left<=right:  ## This will be "and" not "or" otherwise we will get error on [6, 9, 7]
            for i in range(left, right+1):
                new_res.append(matrix[top][i])
            top+=1

            # top to bottom
            for i in range(top, bottom+1):
                new_res.append(matrix[i][right])
            right-=1
            
            # right to left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    new_res.append(matrix[bottom][i])
                bottom-=1

            # bottom to top
            if left <= right:
                for i in range(bottom, top-1, -1):
                    new_res.append(matrix[i][left])
                left+=1

        return new_res


matrix = [[6,9,7]]
c1 =Solution()
print(c1.spiralOrder(matrix))
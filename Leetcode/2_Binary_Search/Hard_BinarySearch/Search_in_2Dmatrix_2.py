'''https://leetcode.com/problems/search-a-2d-matrix-ii/description/'''

''' THis is not a normal matrix. Each row is sorted and each column
But if you will check last element of current row and first element of next row they are not sorted.'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            # print(matrix[i])
            each_row = matrix[i]
            # Set low and high to the INDICES of the row, not the values
            low = 0
            high = col - 1
            while low <= high:
                mid = (low + high) // 2
                # Compare target to the value at the 'mid' index
                if each_row[mid] == target:
                    return True
                if each_row[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        return False

    
matrix =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
c1 = Solution()
print(c1.searchMatrix(matrix, target))

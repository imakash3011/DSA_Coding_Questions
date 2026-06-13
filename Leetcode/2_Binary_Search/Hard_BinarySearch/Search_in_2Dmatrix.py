'''https://leetcode.com/problems/search-a-2d-matrix/description/'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        n = len(matrix)
        m = len(matrix[0])
        
        # Binary Search on an imaginary flattened 1D array
        low = 0
        high = (n * m) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Convert 1D mid-index to 2D matrix coordinates
            row = mid // m
            col = mid % m
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                # Target is greater, search the right half
                low = mid + 1
            else:
                # Target is smaller, search the left half
                high = mid - 1
                
        return False





matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3
c1 = Solution()
print(c1.searchMatrix(matrix, target))

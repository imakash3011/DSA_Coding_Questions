'''https://leetcode.com/problems/find-a-peak-element-ii/'''


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]: 
        row = len(mat)
        max_ele_idx = []
        max_element = float('-inf')
        for i in range(row):
            curr_max = max(mat[i])
            max_idx = mat[i].index(curr_max)
            if mat[i][max_idx]>max_element:
                max_element = mat[i][max_idx]
                max_ele_idx = [i, max_idx]

        return  max_ele_idx



mat =[[1,4],[3,2]]
c1 = Solution()
print(c1.findPeakGrid(mat))



####################### BRUTE FORCE #############################
# class Solution:
#     def findPeakGrid(self, mat: List[List[int]]) -> List[int]: 
#         row = len(mat)
#         col = len(mat[0])
#         max_ele_idx = []
#         max_element = float('-inf')
#         for i  in range(row):
#             for j in range(col):
#                 if max_element < mat[i][j]:
#                     max_element = mat[i][j] 
#                     max_ele_idx = [i,j]

#         return max_ele_idx

        
# mat = [[1,4],[3,2]]
# c1 = Solution()
# print(c1.findPeakGrid(mat))
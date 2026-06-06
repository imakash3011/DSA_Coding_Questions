'''
https://leetcode.com/problems/pascals-triangle/description/
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_output = []

        for i in range(numRows):
            row = [1]*(i+1)   # First element is always 1
            if i>=2:
                prev = final_output[i-1]

                for j in range(1, i):
                    row[j] = prev[j-1] +  prev[j]

            final_output.append(row)

        return final_output
numRows = 5
c1 = Solution()
print(c1.generate(numRows))
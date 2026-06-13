'''https://takeuforward.org/plus/dsa/problems/find-row-with-maximum-1's?source=strivers-a2z-dsa-track'''

class Solution:
    def rowWithMax1s(self, mat):
        if not mat or not mat[0]:
            return -1
            
        n = len(mat)
        m = len(mat[0])
        max_cnt = 0
        index = -1
        
        # Helper function to find the first occurrence of 1
        def lower_bound(arr, m, x):
            low = 0
            high = m - 1
            ans = m
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        # Check each row
        for i in range(n):
            cnt_ones = m - lower_bound(mat[i], m, 1)
            
            if cnt_ones > max_cnt:
                max_cnt = cnt_ones
                index = i
                
        return index
    

mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]
c1 = Solution()
print(c1.rowWithMax1s(mat))
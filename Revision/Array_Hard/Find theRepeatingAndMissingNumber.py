'''
https://takeuforward.org/plus/dsa/problems/find-the-repeating-and-missing-number?source=strivers-a2z-dsa-track
'''

class Solution:
    def findMissingRepeatingNumbers(self, nums):
        result = []
        n = len(nums)
        sum_n = (n*(n+1)//2)
        sum_nums = sum(nums)
        dct = {}
        for i in nums:
            dct[i] = dct.get(i, 0)+1
        repeating_val = 0
        for i,j in dct.items():
            if j==2:
                repeating_val = i
                break
        unique_val_sum_n = sum_nums - repeating_val
        missing_val = sum_n - unique_val_sum_n
        # print(sum_n, sum_nums,repeating_val, unique_val_sum_n, missing_val)
        result.append([repeating_val, missing_val])
                
        return result

nums =  [1, 2, 3, 6, 7, 5, 7]
c1 = Solution()
print(c1.findMissingRepeatingNumbers(nums))



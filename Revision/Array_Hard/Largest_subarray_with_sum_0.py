'''
https://takeuforward.org/plus/dsa/problems/largest-subarray-with-sum-0?source=strivers-a2z-dsa-track
'''

class Solution:
    def maxLen(self, arr):
        n = len(arr)
        max_cnt = 0
        for i in range(n):
            temp = arr[i]
            cnt=1
            for j in range(i+1,n):
                temp+=arr[j]
                cnt+=1
                if temp ==0 and cnt>max_cnt:
                    max_cnt = cnt
        return max_cnt



arr =[2, 10, 4]
c1 = Solution()
print(c1.maxLen(arr))


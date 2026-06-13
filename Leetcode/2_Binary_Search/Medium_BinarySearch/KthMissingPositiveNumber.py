''' 
https://leetcode.com/problems/kth-missing-positive-number/description/
'''

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) -1
        while low<=high:
            mid = (low+high)//2
            missing_val = arr[mid] - (mid+1)
            if missing_val < k:
                low = mid+1
            else:
                high = mid-1
        print(low, k)
        return low+k


arr = [1,2,3,4]
k = 2
c1 = Solution()
print(c1.findKthPositive(arr, k))

######################### LINEAR APPROACH ###########################
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 0
        ans = 1
        result = []
        while cnt<=k :
            if ans not in arr:
                result.append(ans)
                cnt+=1
            ans+=1
        return result[k-1]
        


# arr = [1,2,3,4]
# k = 2
# c1 = Solution()
# print(c1.findKthPositive(arr, k))
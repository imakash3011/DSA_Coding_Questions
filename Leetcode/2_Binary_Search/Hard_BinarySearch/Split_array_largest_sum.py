'''https://leetcode.com/problems/split-array-largest-sum/description/'''

''' This split array largest sum and the painters partition is same'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums)<k:
            return -1
        
        def count_subarrays(nums, mid):
            # Helper function to count how many subarrays we need 
            # if the maximum allowed sum is 'mid'
            n = len(nums)
            curr_sum = 0
            subarrays = 1
            for i in range(n):
                if nums[i]+curr_sum<=mid:
                    curr_sum += nums[i]
                else:
                    # If adding this number exceeds mid, start a new subarray
                    subarrays +=1
                    curr_sum = nums[i]
            return subarrays

        low = max(nums)   # Minimum possible answer is the largest single element
        high = sum(nums)
        while low<= high:
            mid = (low+high)//2
            num_subarray_done = count_subarrays(nums, mid)
            if num_subarray_done<=k:
                high= mid-1   # 'mid' is a valid answer, but try to find a smaller one
            else:
                low = mid+1  # 'mid' is too small, we need a larger max sum to reduce the number of subarrays
        return low

    

nums = [7,2,5,10,8]
k = 2
c1 = Solution()
print(c1.splitArray(nums, k))
'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
'''


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def day_fit(weights ,capacity ):
            day = 1
            load = 0
            n = len(weights)
            for i in range(n):
                if load + weights[i] > capacity:  ## is exceeding the capacity go to next day
                    day +=1
                    load = weights[i]
                else:
                    load += weights[i]
            return day
        
        left = max(weights)
        right = sum(weights)
        while left<=right:   ## This loop is running on the hypothatical array which is being created by left and write... 
            mid = (left+right)//2
            result = day_fit(weights, mid)  ## If you'll assign this much capacity then how many days it will take to deliver
            if result<=days: # if possible lets look for even smaller
                right = mid-1
            else:   # If not possible let's find bigger number
                left = mid+1
                
        return left
    
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
c1 = Solution()
print(c1.shipWithinDays(weights, days))
'''https://leetcode.com/problems/combination-sum-iii/description/'''



class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        nums = [1,2,3,4,5,6,7,8,9]
        
        def helper_func(nums,idx,total, k, n, subset):

            if len(subset) == k and total==n:
                result.append(subset.copy())
                return
            
            if idx>=len(nums) or total>n or len(subset)>k:
                return
            
            subset.append(nums[idx])
            helper_func(nums,idx+1,total + nums[idx],  k, n, subset)

            subset.pop()
            helper_func(nums,idx+1, total, k, n, subset)
        
        helper_func(nums,0,0, k, n, [])
        return result


k = 3 
n = 7
c1 = Solution()
print(c1.combinationSum3(k, n))



################### ANOTHER APPROACH #################


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, target: int, current_combination: List[int]):
            # Base Case: Valid combination found
            if len(current_combination) == k:
                if target == 0:
                    result.append(list(current_combination))
                return
            
            # Pruning Optimization: If target becomes negative, no point in continuing
            if target < 0:
                return
            
            # Loop through available numbers from 'start' to 9
            for num in range(start, 10):
                # Optimization: If the current number is greater than the remaining target,
                # then all subsequent numbers will also be too large. We can break early.
                if num > target:
                    break
                    
                current_combination.append(num)
                # Recurse with num + 1 to ensure unique elements
                backtrack(num + 1, target - num, current_combination) 
                current_combination.pop() # Backtrack
                
        backtrack(1, n, [])
        return result
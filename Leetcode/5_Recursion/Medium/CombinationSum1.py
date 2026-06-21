'''https://leetcode.com/problems/combination-sum/description/'''



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper_func(idx, total, subset):
            if total == target:
                result.append(subset.copy())
                return

            if idx>=len(candidates) or total>target:
                return
            
            subset.append(candidates[idx])
            helper_func(idx, total + candidates[idx], subset)

            subset.pop()
            helper_func(idx+1, total, subset)
        
        helper_func(0, 0, [])
        return result



candidates = [2,3,5] 
target = 8
c1 = Solution()
print(c1.combinationSum(candidates, target))
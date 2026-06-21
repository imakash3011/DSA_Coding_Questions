from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # HIGHLIGHT 1: We must sort the array first so duplicates are adjacent.
        candidates.sort()
        
        def helper_func(idx, total, subset):
            if total == target:
                # HIGHLIGHT 2: Cleaned up the 'not in' check. 
                # Our skipping logic guarantees uniqueness, making this O(1).
                result.append(subset.copy())
                return

            if idx >= len(candidates) or total > target:
                return
            
            # --- CHOICE 1: INCLUDE candidates[idx] ---
            subset.append(candidates[idx])  
            helper_func(idx + 1, total + candidates[idx], subset)
            subset.pop() # Backtrack

            # --- CHOICE 2: EXCLUDE candidates[idx] ---
            # HIGHLIGHT 3: Instead of blindly going to idx + 1, skip all duplicate 
            # elements. This prevents the code from generating identical combinations. When it backtrack it prevent formating same numbers means if 1,2 is done then while backtracking we will prevent further
            next_idx = idx + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
                next_idx += 1
                
            helper_func(next_idx, total, subset)

        
        helper_func(0, 0, [])
        return result

# Test case
candidates = [2, 5, 2, 1, 2]
target = 5
c1 = Solution()
print(c1.combinationSum2(candidates, target))
# Output: [[1, 2, 2], [5]]




'''
The while loop breakthrough: If your sorted array is [1, 2, 2, 2, 5] and you are at the first 2 (idx=1), 
your code explores what happens when you include it. When you backtrack to exclude it, you want to skip 
all remaining 2s at this level. The while loop fast-forwards next_idx straight to the 5, completely bypassing 
the identical branches that caused your duplicates.
'''


################# ANOTHER SOLUTION ###############
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # HIGHLIGHT 1: We must sort the array first so duplicates are adjacent.
        candidates.sort()
        
        def helper_func(idx, total, subset):
            if total == target:
                if subset not in result:
                # HIGHLIGHT 2: Cleaned up the 'not in' check. 
                # Our skipping logic guarantees uniqueness, making this O(1).
                    result.append(subset.copy())
                return

            if idx >= len(candidates) or total > target:
                return
            
            # --- CHOICE 1: INCLUDE candidates[idx] ---
            subset.append(candidates[idx])  
            helper_func(idx + 1, total + candidates[idx], subset)
            subset.pop() # Backtrack

            # --- CHOICE 2: EXCLUDE candidates[idx] ---
            # HIGHLIGHT 3: Instead of blindly going to idx + 1, skip all duplicate 
            # elements. This prevents the code from generating identical combinations. When it backtrack it prevent formating same numbers means if 1,2 is done then while backtracking we will prevent further
            # next_idx = idx + 1
            # while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
            #     next_idx += 1
                
            # helper_func(next_idx, total, subset)
            helper_func(idx+1, total, subset)
        
        helper_func(0, 0, [])
        return result

# Test case
# candidates = [2, 5, 2, 1, 2]
# target = 5
# c1 = Solution()
# print(c1.combinationSum2(candidates, target))
# Output: [[1, 2, 2], [5]]

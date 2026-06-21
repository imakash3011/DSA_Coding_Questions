'''https://leetcode.com/problems/subsets-ii/?envType=problem-list-v2&envId=bit-manipulation'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 1. Crucial step: Sort the array to group duplicates together
        nums.sort()
        
        n = len(nums)
        total_subsets = 1 << n
        all_subsets = []
        
        for i in range(total_subsets):
            curr_subset = []
            is_valid = True
            
            for j in range(n):
                # Check if the j-th bit is set
                if (i & (1 << j)) != 0:
                    # Duplicate handling rule:
                    # If this element is a duplicate of the previous one...
                    # ...and the previous element was NOT picked (the (j-1)-th bit in i is 0)
                    if j > 0 and nums[j] == nums[j-1] and (i & (1 << (j - 1))) == 0:
                        is_valid = False
                        break  # Prune this subset invalid pattern immediately
                    
                    curr_subset.append(nums[j])
            
            # Only append if it passed our duplicate-pruning condition
            if is_valid:
                all_subsets.append(curr_subset)
                
        return all_subsets
    

nums = [4,4,4,1,4]
c1 = Solution()
print(c1.subsetsWithDup(nums))
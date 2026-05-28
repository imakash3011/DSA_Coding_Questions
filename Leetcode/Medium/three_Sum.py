'''
https://leetcode.com/problems/3sum/description/
'''

####################### OPTIMAL APPROACH (we need to skip value which are same when moving pointer) ###############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # if standing i and before moving i to next iteration check whether next value is same or not...becz same value will end up giving same answer
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:  ## This is triplet condition and the reason why we're not reducing k here because it 
                    ## is automatically getting handled by right-=1. Means at any point of j if triplet is getting formed the when we move forward the value will  be either = or >0 means total will also become >0 and this is where right-=1 is getting done.
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res

nums =[-1,0,1,2,-1,-4]
c1 = Solution()
print(c1.threeSum(nums))


####################### SLIGHTLY BETTER APPROACH ###############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n):
                target = -(nums[i]+nums[j])
                if target in nums[j+1:]:
                    sorted_lst = sorted([nums[i], nums[j],  target])
                    if sorted_lst not in result:
                        result.append(sorted_lst)
        return result

# nums =[-1,0,1,2,-1,-4]
# c1 = Solution()
# print(c1.threeSum(nums))



####################### BRUTE FORCE ###############################

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans = [nums[i], nums[j], nums[k]]
                        sorted_ans = sorted(ans) # Sort it first
                        if sorted_ans not in result:
                            result.append(sorted_ans) # Append the sorted version
        return result

# nums =[-1,0,1,2,-1,-4]
# c1 = Solution()
# print(c1.threeSum(nums))
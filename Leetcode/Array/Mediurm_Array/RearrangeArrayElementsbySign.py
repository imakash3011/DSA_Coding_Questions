class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0]*n
        neg, pos =1, 0
        for num in nums:
            if num>0:
                res[pos] = num
                pos+=2
                if pos>n:
                    pos =0
            else:
                res[neg] = num
                neg+=2
                if neg>n:
                    neg =0
        return res

nums = [-1,1]
c1 = Solution()
print(c1.rearrangeArray(nums))
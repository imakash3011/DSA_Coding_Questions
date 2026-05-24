class Solution:
    def countFrequencies(self, nums):
        dct = {}
        for i in nums:
            dct[i] = dct.get(i ,0 )+1
        
        result = []
        for i,j in dct.items():
            if [i,j] not in result:
                result.append([i,j])
        return result
    
c1 = Solution()
print(c1.countFrequencies([1, 2, 2, 1, 3]))
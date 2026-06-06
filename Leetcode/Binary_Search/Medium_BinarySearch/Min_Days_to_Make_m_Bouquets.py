'''
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
'''

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible_flower(bloomDay: List[int], days: int, m: int, k: int)->int:
            flower_possible = 0
            cnt= 0
            n = len(bloomDay)
            for i in range(n):
                
                if bloomDay[i] <=days:
                    cnt+=1
                else:
                    flower_possible += cnt//k
                    cnt = 0
            flower_possible +=cnt//k
            # print(flower_possible)
            if flower_possible>=m:
                return True
            else:
                return False 
        
        # return result
        left = min(bloomDay)
        right = max(bloomDay)
        while left<=right:
            mid = (left+right)//2
            result = possible_flower(bloomDay, mid,m,k)
            if result == True:
                right = mid-1
            else:
                left = mid+1
        if left in bloomDay:
            return left
        else:
            return -1            

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
c1 = Solution()
print(c1.minDays(bloomDay, m, k))

        



































# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         def possible_flower(bloomDay: List[int], days: int, m: int, k: int)->int:
#             flower_possible = 0
#             cnt= 0
#             n = len(bloomDay)
#             for i in range(n):
                
#                 if bloomDay[i] <=days:
#                     cnt+=1
#                 else:
#                     flower_possible += cnt//k
#                     cnt = 0
#             flower_possible +=cnt//k
#             print(flower_possible)
#             if flower_possible>=m:
#                 return True
#             else:
#                 return False 
#         result = possible_flower(bloomDay, 13,2,3)
#         return result

# bloomDay = [7, 7,7,7,13,11,12,7]
# m = 2
# k = 3
# c1 = Solution()
# print(c1.minDays(bloomDay, m, k))

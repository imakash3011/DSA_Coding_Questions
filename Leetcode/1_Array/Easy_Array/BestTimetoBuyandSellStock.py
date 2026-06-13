
'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         n = len(prices)

#         if n==1:
#             return 0

#         for i in range(n):
#             temp = prices[i]
#             for j in range(i+1,n):
#                 #   max_profit = max(max_profit,prices[j]-temp ) ## instead of following if condition use this method
#                 if prices[j]-temp>max_profit:
#                     max_profit = prices[j]-temp
#         return max_profit



# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         n = len(prices)
#         for i in range(n-1):
#             temp = prices[i]
#             max_ele = max(prices[i+1:])  ## This slicing will be O(n) and outer loop will be make it O(n^2)
#             max_profit = max(max_profit,max_ele-temp )
#         return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price<min_price:
                min_price = price
            if price-min_price>max_profit:
                max_profit = price -min_price
        return max_profit

prices =[10, 7, 5, 8, 11, 9]
c1 = Solution()
print(c1.maxProfit(prices))
        
def best_stock_selling(prices):
    n = len(prices)
    profit = 0
    # Initialize to positive infinity so any price will be smaller
    min_price = float('inf') 
    
    for i in range(n):
        # Update the lowest price seen so far
        min_price = min(min_price, prices[i])
        
        # Calculate potential profit if we sold today
        current_profit = prices[i] - min_price
        
        # Update maximum profit seen so far
        profit = max(profit, current_profit)
    
    return profit

prices = [7, 2, 1, 5, 6, 4, 8]
print(best_stock_selling(prices))  # Output: 7 (Buy at 1, Sell at 8)

#########################################

def sell_stock(prices):
    n = len(prices)
    profit = 0
    for i in range(n):
        for j in range(n):
            if j>i and prices[j]-prices[i] > profit:
                profit = prices[j]-prices[i]
    return profit


# # prices = [8,5,3,2,1]
# prices = [7,2,1,5,6,4,8]
# print(sell_stock(prices))     



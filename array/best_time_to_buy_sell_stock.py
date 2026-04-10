# Problem: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        
        return max_profit

# notes:
# idea: we want to buy at the lowest price and sell at the highest AFTERR that

# we keep track of the lowest price weve seen so far (min_price)
# then for each price:
#  if its lower than min_price >> update min_price (better buying point)
#  else >> calculate profit if we sell now

# profit = current price, min_price

# we keep updating max_profit if we find a better one

# example:
# prices = [7,1,5,3,6,4]
# start:
# min_price = inf, max_profit = 0

# 7 >> min_price = 7
# 1 >> min_price = 1 (u better buy)
# 5 >> profit = 5 - 1 = 4 → max_profit = 4
# 3 >> profit = 3 - 1 = 2 (js ignore)
# 6 >> profit = 6 - 1 = 5 → max_profit = 5
# 4 >> profit = 4 - 1 = 3 (ignore)

# final answer = 5

# so why this works:
# i only go through the list once (1 pass)
# always making the best decision at each step

# complexity:
# time: O(n) >> one loop
# space: O(1) >> no extra data structure
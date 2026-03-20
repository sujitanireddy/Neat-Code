#Question -> https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        L = 0
        R = 1
        max_profit_by_far = 0

        while R < len(prices):

            if prices[L] < prices[R]:

                profit = prices[R] - prices[L]

                max_profit_by_far = max(max_profit_by_far, profit)
            
            else:

                L = R
            
            R += 1 
        
        return max_profit_by_far




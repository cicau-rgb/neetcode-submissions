class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best_profit = 0

        for price in prices[1::]:
            if min_price > price:
                min_price = price
            elif price - min_price > best_profit:
                best_profit = price - min_price
        
        return best_profit
        



        
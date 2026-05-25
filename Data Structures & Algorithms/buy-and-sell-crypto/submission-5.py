class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0 
        left, right = 0,1 

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_price = max(max_price, profit)
            else: 
                left = right
            right += 1 
        return max_price 
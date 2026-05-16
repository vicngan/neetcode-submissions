class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #initialize left and right at 0, 1 index 
        maxp = 0 #max profit starts at 0

        while r < len(prices):  #if the right index less than list of prices
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] #profit = big-small
                maxp = max(maxp, profit) #max profit = maximum value of max profit and the number itself 
            else:
                l = r #if prices of l is more than r, initialize l to be the new r because it's lower 
            r+=1 #move r pointer 1 
        return maxp
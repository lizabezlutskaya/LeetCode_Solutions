class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        
        minprice = prices[0]
        maxprofit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                curr = prices[i] - minprice
                if curr > maxprofit: maxprofit = curr
                    
        return maxprofit
                
                
        
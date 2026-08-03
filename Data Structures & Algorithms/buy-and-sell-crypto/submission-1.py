class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            j = i +1
            while(j < len(prices)):
                diff = prices[j] - prices[i]
                if(diff > 0):
                    res = max(diff, res)
                
                j += 1
        
        return res
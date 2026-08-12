class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        b =0
        s=1

        while s<=len(prices)-1:
            if prices[s] <=prices[b]:
                b=s
                s+=1
            elif prices[b]<=prices[s] :
                max_profit = max(max_profit,prices[s]-prices[b])
                s+=1
            
        return max_profit

        
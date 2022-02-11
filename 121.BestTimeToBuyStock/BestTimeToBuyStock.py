class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxP=0
        
        while r<len(prices):
            if prices[l] < prices [r]:
                profit = prices [r] - prices [l]
                maxP = max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP
        
        
        
#         min1_index=(prices.index(min(prices)))
#         min_num=min(prices)
        
#         max_num=(max(prices[min1_index:]))
        
#         if (min1_index==len(prices)-1): return 0
#         else: return max_num-min_num
        
        
        
        
        
        
        
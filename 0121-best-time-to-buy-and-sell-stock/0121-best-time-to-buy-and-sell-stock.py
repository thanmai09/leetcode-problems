class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            ans = max(ans,prices[i]-low)
            low = min(low,prices[i])
        return ans
        
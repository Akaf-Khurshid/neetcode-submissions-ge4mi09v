class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 101
        sell = 0
        maxx = 0
        for i in prices:
            if i < buy:
                buy = i
                sell = i
            if i > sell:
                sell = i
                maxx = max(maxx, sell - buy)
        return maxx
        
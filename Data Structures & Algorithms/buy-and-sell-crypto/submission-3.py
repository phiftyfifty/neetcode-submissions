class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        n = len(prices)
        left, right = 0, 1
        while right < n:
            # possible profit
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_p = max(profit, max_p)
            # no profit, find another window
            else:
                left = right
            right += 1
        return max_p
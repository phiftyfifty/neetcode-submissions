class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(N) time
        # O(1) space
        max_p = 0
        n = len(prices)
        min_buy = prices[0]

        for price in prices:
            # buy it at this min
            min_buy = min(min_buy, price)
            # sell it for the best profit
            max_p = max(price - min_buy, max_p)
        return max_p
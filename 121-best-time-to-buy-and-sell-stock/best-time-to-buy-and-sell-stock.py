class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = prices[0]
        profit = 0

        for price in prices:
            if price < minimum:
                minimum = price
            else:
                current_profit = price - minimum
                profit = max(profit, current_profit)
        return profit
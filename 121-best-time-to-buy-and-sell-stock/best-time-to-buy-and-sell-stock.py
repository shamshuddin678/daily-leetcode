class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr = 0
        max_profit = 0

        for i in range(1,len(prices)):
            curr = max(0,curr + prices[i] - prices [i - 1])
            max_profit = max(max_profit,curr)
        return max_profit 
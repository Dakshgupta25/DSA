class Solution(object):
    def maxProfit(self, prices, fee):
        n = len(prices)

        after = [0] * 2

        for day in range(n-1, -1, -1):
            cur = [0] * 2

            # Can buy
            cur[1] = max(
                -prices[day] + after[0],
                after[1]
            )

            # Can sell
            cur[0] = max(
                prices[day] - fee + after[1],
                after[0]
            )

            after = cur

        return after[1]
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)

        after = [[0]*3 for _ in range(2)]

        for day in range(n-1, -1, -1):
            cur = [[0]*3 for _ in range(2)]

            for buy in range(2):
                for cap in range(1, 3):

                    if buy:
                        cur[buy][cap] = max(
                            -prices[day] + after[0][cap],
                            after[1][cap]
                        )
                    else:
                        cur[buy][cap] = max(
                            prices[day] + after[1][cap-1],
                            after[0][cap]
                        )

            after = cur

        return after[1][2]
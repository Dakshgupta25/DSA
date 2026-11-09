class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)

        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]

        for day in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):

                    if buy:
                        dp[day][buy][cap] = max(
                            -prices[day] + dp[day+1][0][cap],
                            dp[day+1][1][cap]
                        )
                    else:
                        dp[day][buy][cap] = max(
                            prices[day] + dp[day+1][1][cap-1],
                            dp[day+1][0][cap]
                        )

        return dp[0][1][2]
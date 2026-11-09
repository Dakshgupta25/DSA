class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        memo=[[[-1]*3 for _ in range(2)] for _ in range(n)]

        def dp(day,buy,cap):
            if cap==0 or day>=n:
                return 0
            if memo[day][buy][cap]!=-1:
                return memo[day][buy][cap]
            if buy:
                ans = max(
                    -prices[day] + dp(day+1, 0, cap),
                    dp(day+1, 1, cap)
                )
            else:
                ans = max(
                    prices[day] + dp(day+1, 1, cap-1),
                    dp(day+1, 0, cap)
                )

            memo[day][buy][cap] = ans
            return ans

        return dp(0, 1, 2)
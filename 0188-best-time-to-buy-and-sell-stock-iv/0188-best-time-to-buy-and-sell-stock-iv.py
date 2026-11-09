class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        after = [[0]*(k+1) for _ in range(2)]

        for day in range(n-1, -1, -1):
            cur = [[0]*(k+1) for _ in range(2)]

            for buy in range(2):
                for cap in range(1, k+1):

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

        return after[1][k]
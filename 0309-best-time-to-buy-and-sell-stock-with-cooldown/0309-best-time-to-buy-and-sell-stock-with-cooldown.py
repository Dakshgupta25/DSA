class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)

        after = [0] * 2
        after2 = [0] * 2

        for day in range(n-1, -1, -1):
            cur = [0] * 2

            # Can buy
            cur[1] = max(
                -prices[day] + after[0],
                after[1]
            )

            # Can sell (cooldown: skip next day)
            cur[0] = max(
                prices[day] + after2[1],
                after[0]
            )

            after2 = after
            after = cur

        return after[1]
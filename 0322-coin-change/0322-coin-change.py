class Solution(object):
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[-1] * (amount + 1) for i in range(n)]

        def solve(ind, cur):

            # Base case
            if ind == 0:
                if cur % coins[0] == 0:
                    return cur // coins[0]
                return float("inf")

            # Memoization check
            if dp[ind][cur] != -1:
                return dp[ind][cur]

            # Not take
            notake = solve(ind - 1, cur)

            # Take (same index because unlimited coins)
            take = float("inf")
            if coins[ind] <= cur:
                take = 1 + solve(ind, cur - coins[ind])

            dp[ind][cur] = min(take, notake)
            return dp[ind][cur]

        ans = solve(n - 1, amount)

        if ans == float("inf"):
            return -1

        return ans


            

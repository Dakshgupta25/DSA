class Solution(object):
    def change(self, amount, coins):
        n = len(coins)
        dp = {}

        def solve(ind, cur):
            if cur == amount:
                return 1

            if ind == n or cur > amount:
                return 0

            if (ind, cur) in dp:
                return dp[(ind, cur)]

            take = solve(ind, cur + coins[ind])
            not_take = solve(ind + 1, cur)

            dp[(ind, cur)] = take + not_take

            return dp[(ind, cur)]

        return solve(0, 0)

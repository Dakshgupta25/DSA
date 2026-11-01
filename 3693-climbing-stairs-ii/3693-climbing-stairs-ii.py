class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
    
        """
class Solution(object):
    def climbStairs(self, n, costs):

        dp = [-1] * (n+1)

        def lol(i):

            if i == 0:
                return 0

            if dp[i] != -1:
                return dp[i]

            if i == 1:
                dp[i] = costs[0] + 1
                return dp[i]

            if i == 2:
                two = 4 + lol(i-2)
                one = 1 + lol(i-1)

                dp[i] = costs[i-1] + min(two, one)
                return dp[i]

            three = 9 + lol(i-3)
            two = 4 + lol(i-2)
            one = 1 + lol(i-1)

            dp[i] = costs[i-1] + min(three, two, one)
            return dp[i]

        return lol(n)
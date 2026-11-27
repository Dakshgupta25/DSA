class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        n = len(str1)
        m = len(str2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Build LCS table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        ans = ""

        # Reconstruct SCS
        while n > 0 and m > 0:
            if str1[n-1] == str2[m-1]:
                ans += str1[n-1]
                n -= 1
                m -= 1

            elif dp[n-1][m] > dp[n][m-1]:
                ans += str1[n-1]
                n -= 1

            else:
                ans += str2[m-1]
                m -= 1

        # Add remaining characters
        while n > 0:
            ans += str1[n-1]
            n -= 1

        while m > 0:
            ans += str2[m-1]
            m -= 1

        return ans[::-1]



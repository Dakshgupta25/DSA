class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """

        def isprime(x):
            if x < 2:
                return False

            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1

            return True

        n = len(nums)
        res = 0

        for i in range(n):
            # Main diagonal
            x = nums[i][i]
            if isprime(x):
                res = max(res, x)

            # Secondary diagonal
            x = nums[i][n - 1 - i]
            if isprime(x):
                res = max(res, x)

        return res


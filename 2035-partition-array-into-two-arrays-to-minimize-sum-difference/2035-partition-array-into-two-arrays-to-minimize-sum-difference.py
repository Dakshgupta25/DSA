
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums):
        n = len(nums)
        total = sum(nums)
        m = n // 2

        # Divide array into two halves
        left = nums[:m]
        right = nums[m:]

        # Store sums based on number of selected elements
        leftSum = [[] for _ in range(m + 1)]
        rightSum = [[] for _ in range(m + 1)]

        # Generate subset sums using recursion
        def solve(arr, ind, count, s1, res):

            # All elements processed
            if ind == len(arr):
                res[count].append(s1)
                return

            # Take current element
            solve(arr, ind + 1, count + 1, s1 + arr[ind], res)

            # Not take current element
            solve(arr, ind + 1, count, s1, res)

        # Generate sums for both halves
        solve(left, 0, 0, 0, leftSum)
        solve(right, 0, 0, 0, rightSum)

        # Sort right subset sums
        for arr in rightSum:
            arr.sort()

        ans = float('inf')

        # Select i elements from left half
        for i in range(m + 1):

            # Select remaining elements from right half
            j = m - i

            for s1 in leftSum[i]:

                # Ideal sum required from right half
                target = (total - 2 * s1) / 2

                arr = rightSum[j]

                # Binary search
                pos = bisect_left(arr, target)

                # Check closest sum on right
                if pos < len(arr):
                    s = s1 + arr[pos]
                    ans = min(ans, abs(total - 2 * s))

                if pos > 0:
                    s = s1 + arr[pos - 1]
                    ans = min(ans, abs(total - 2 * s))

        return ans

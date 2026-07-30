class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        maxCost = max(costs)
        arr = [0] * (maxCost + 1)

        for cost in costs:
            arr[cost] += 1

        ans = 0

        for cost, count in enumerate(arr):
            if count == 0:
                continue

            canBuy = min(count, coins // cost)

            ans += canBuy
            coins -= canBuy * cost

            if coins < cost:
                break

        return ans
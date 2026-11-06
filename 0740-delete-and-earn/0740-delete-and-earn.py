class Solution(object):
    def deleteAndEarn(self, nums):
        dic = {}

        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        dic = dict(sorted(dic.items()))

        twoback = 0
        oneback = 0
        prev = -1

        for key, value in dic.items():
            points = key * value

            if key == prev + 1:
                curr = max(oneback, twoback + points)
            else:
                curr = oneback + points

            twoback = oneback
            oneback = curr
            prev = key

        return oneback
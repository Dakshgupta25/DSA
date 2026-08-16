class Solution(object):
    def hasGroupsSizeX(self, deck):
        dic = {}

        for i in deck:
            dic[i] = dic.get(i, 0) + 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        x = 0

        for count in dic.values():
            x = gcd(x, count)

        return x > 1
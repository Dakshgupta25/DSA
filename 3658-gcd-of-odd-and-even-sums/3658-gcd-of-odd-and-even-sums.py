class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        even=n*(n+1)
        odd=n*n

        while odd:
            even,odd=odd,even%odd
        return even

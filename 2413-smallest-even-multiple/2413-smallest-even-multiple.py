class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=n
        while True:
            if n%2==0:
                return n
            n+=i
    
        
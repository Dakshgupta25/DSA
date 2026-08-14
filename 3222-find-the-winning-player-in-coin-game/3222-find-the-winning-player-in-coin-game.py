class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        if min(x,y//4)%2==0:
            return "Bob"
        else:
            return "Alice"
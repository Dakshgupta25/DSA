class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        alice = 0
        bob = 0

        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i] == colors[i+1] == 'A':
                alice += 1
            elif colors[i-1] == colors[i] == colors[i+1] == 'B':
                bob += 1

        return alice > bob
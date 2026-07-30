class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        steps = 0
        while target > startValue:
            steps += 1 + target % 2 # if target not divisible do 1 extra step (add one to target)
            target += target % 2 # if target not divisible add one to target
            target //= 2
            
        return steps + (startValue - target)
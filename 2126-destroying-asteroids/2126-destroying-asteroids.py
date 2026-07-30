class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort(reverse=True)
        cur=sum(asteroids)
        for i in asteroids:
            if cur-i+mass<i:
                return False
            else:
                cur-=i
        return True
            
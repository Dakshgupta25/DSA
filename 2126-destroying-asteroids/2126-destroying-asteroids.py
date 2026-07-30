class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for i in asteroids:
            if i > mass:
                return False
            mass += i
        return True
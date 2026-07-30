class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(reverse=True)
        i=0
        j=len(people)-1
        while i<=j:
            if people[i]+people[j]<=limit:
                j-=1
            i+=1
            
        return i

class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        res=[]
        i=1
        while i<n:
            for j in range(i+1,n+1):
                if gcd(i,j)<=1:
                    res.append(str(i)+"/"+str(j))
            i+=1
        return res
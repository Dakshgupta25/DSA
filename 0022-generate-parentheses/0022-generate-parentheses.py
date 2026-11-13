class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def fun(l,r,cur):
            if l==r==0:
                res.append(cur)
                return 
            if l>0:
                fun(l-1,r,cur+"(")
            if l<r and r>0:
                fun(l,r-1,cur+")")
            return         
        fun(n,n,"")
        return res
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(image)
        m=len(image[0])
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            k=0
            for j in range(m-1,-1,-1):
                res[i][k]= 1 - image[i][j]
                k+=1
        return res
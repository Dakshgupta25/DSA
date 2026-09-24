class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(heights)
        m = len(heights[0])

        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]

        def dfs(i, j, visited):
            # Boundary check
            if i < 0 or i >= n or j < 0 or j >= m:
                return

            if visited[i][j]:
                return

            visited[i][j] = True

            # Move to cells with equal or greater height
            if i > 0 and heights[i - 1][j] >= heights[i][j]:
                dfs(i - 1, j, visited)

            if i < n - 1 and heights[i + 1][j] >= heights[i][j]:
                dfs(i + 1, j, visited)

            if j > 0 and heights[i][j - 1] >= heights[i][j]:
                dfs(i, j - 1, visited)

            if j < m - 1 and heights[i][j + 1] >= heights[i][j]:
                dfs(i, j + 1, visited)

        # Pacific Ocean: top row + left column
        for i in range(n):
            dfs(i, 0, pacific)

        for j in range(m):
            dfs(0, j, pacific)

        # Atlantic Ocean: bottom row + right column
        for i in range(n):
            dfs(i, m - 1, atlantic)

        for j in range(m):
            dfs(n - 1, j, atlantic)

        # Cells reachable from both oceans
        ans = []

        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans
        
        
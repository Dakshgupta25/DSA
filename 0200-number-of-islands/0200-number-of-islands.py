class Solution(object):
    def numIslands(self, grid):
        
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        count = 0

        def dfs(r, c):
            
            # Outside the grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            # Water or already visited
            if grid[r][c] == "0" or visited[r][c]:
                return
            
            visited[r][c] = True

            # Up
            dfs(r - 1, c)

            # Down
            dfs(r + 1, c)

            # Left
            dfs(r, c - 1)

            # Right
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    count += 1

        return count
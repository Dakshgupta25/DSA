class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row = len(grid)
        col = len(grid[0])

        queue = deque()
        fresh = 0

        # Put all rotten oranges into queue
        for i in range(row):
            for j in range(col):

                if grid[i][j] == 2:
                    queue.append((i, j))

                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        # BFS
        while queue and fresh > 0:

            for _ in range(len(queue)):

                i, j = queue.popleft()

                for di, dj in directions:

                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < row and 0 <= nj < col:
                        
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            fresh -= 1
                            queue.append((ni, nj))

            minutes += 1

        if fresh == 0:
            return minutes

        return -1
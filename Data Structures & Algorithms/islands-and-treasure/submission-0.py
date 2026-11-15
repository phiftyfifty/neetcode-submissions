class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # perform bfs for each island
        def bfs(r, c):
            q = deque([(r, c)])
            # Keep track of the visited on this particualr island
            visit = [[False] * cols for _ in range(rows)]
            visit[r][c] = True
            dist = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    # found a chest 
                    if grid[row][col] == 0:
                        return dist
                    for dr, dc in dirs:
                        nr, nc = dr + row, dc + col
                        if (0 <= nr < rows and 0 <= nc < cols and not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                # every layer => + 1 distance
                dist += 1
            return INF
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
                



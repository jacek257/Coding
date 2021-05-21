class Solution:
    def search(self, grid, m, n, i, j):
        grid[i][j] = '-1'

        if ((i-1) >= 0) and (grid[i-1][j] == '1'):
            self.search(grid, m, n, i-1, j)

        if ((j-1) >= 0) and (grid[i][j-1] == '1'):
            self.search(grid, m, n, i, j-1)

        if ((i+1) < m) and (grid[i+1][j] == '1'):
            self.search(grid, m, n, i+1, j)

        if ((j+1) < n) and (grid[i][j+1] == '1'):
            self.search(grid, m, n, i, j+1)


    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == '1'):
                    count += 1
                    self.search(grid, m, n, i, j)

        return count

        

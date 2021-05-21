class Solution {

    void search(char[][] grid, int m, int n, int i, int j) {

        if (i<0 || j<0 || i>=m || j>=n || grid[i][j] == '0') {
            return;
        }

        grid[i][j] = '0';
        search(grid, m, n, i-1, j);
        search(grid, m, n, i, j-1);
        search(grid, m, n, i+1, j);
        search(grid, m, n, i, j+1);
    }

    public int numIslands(char[][] grid) {

        int count = 0;
        int m = grid.length;
        int n = grid[0].length;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == '1') {
                    count++;
                    search(grid, m, n, i, j);
                }
            }
        }

        return count;
    }
}

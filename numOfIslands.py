class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        def dfs(grid: List[List[str]], i: int, j: int) -> int:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
                return 0
        
            grid[i][j] = '0'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        
            return 1
        
        totalIslands = 0
        for i in range(0, len(grid), 1):
            for j in range(0, len(grid[i]), 1):
                if grid[i][j] == '1':
                    totalIslands += dfs(grid, i, j)
        
        return(totalIslands)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visited:
                    count+=1
                    dfs(i,j)
        return count



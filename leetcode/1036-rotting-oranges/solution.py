from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque(())
        fresh = 0
        max_min = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                if grid[i][j]==1:
                    fresh+=1
        while queue:
            row,col,minutes = queue.popleft()
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            max_min = max(max_min,minutes)
            for dr,dc in directions:
                nr = row+dr
                nc = col+dc
                if (0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1):
                    grid[nr][nc]=2
                    fresh-=1
                    queue.append((nr,nc,minutes+1))
        if fresh>0:
            return -1
        else:
            return max_min






from typing import List
from collections import defaultdict

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        
        # dp[i][j] = {cost: max_score}
        dp = [[defaultdict(int) for _ in range(m)] for _ in range(n)]
        
        # Initialize start
        start_cost = 0 if grid[0][0] == 0 else 1
        start_score = grid[0][0]
        
        if start_cost <= k:
            dp[0][0][start_cost] = start_score
        
        for i in range(n):
            for j in range(m):
                for cost, score in list(dp[i][j].items()):
                    
                    for dx, dy in [(1, 0), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        
                        if ni < n and nj < m:
                            val = grid[ni][nj]
                            
                            add_cost = 0 if val == 0 else 1
                            add_score = val
                            
                            new_cost = cost + add_cost
                            new_score = score + add_score
                            
                            if new_cost <= k:
                                if dp[ni][nj][new_cost] < new_score:
                                    dp[ni][nj][new_cost] = new_score
        
        # Answer = max score at bottom-right with cost ≤ k
        res = -1
        for cost, score in dp[n-1][m-1].items():
            res = max(res, score)
        
        return res
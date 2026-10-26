from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visited = [[False * cols for _ in range(cols)] for _ in range(rows)] # wait, let's write standard python initialization
        
        # Proper visited matrix initialization:
        visited = [[False] * cols for _ in range(rows)]
        count = 0
        
        # 4-directional movement: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(rows):
            for c in range(cols):
                # If we find land that hasn't been visited yet, start exploring the island
                if grid[r][c] > 0 and not visited[r][c]:
                    island_sum = 0
                    queue = deque([(r, c)])
                    visited[r][c] = True
                    
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        island_sum += grid[curr_r][curr_c]
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            # Check boundaries, whether it's land (> 0), and if it's unvisited
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                    
                    # Check if the total island value is divisible by k
                    if island_sum % k == 0:
                        count += 1
                        
        return count
        

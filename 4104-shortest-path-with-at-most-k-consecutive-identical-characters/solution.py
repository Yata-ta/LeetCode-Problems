import heapq
from math import inf
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build the adjacency list
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            
        # dist[u][cur] stores the minimum weight to reach node u 
        # with 'cur' consecutive identical characters ending the path.
        dist = [[inf] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        
        # Priority queue stores tuples of (accumulated_weight, current_node, consecutive_count)
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, cur = heapq.heappop(pq)
            
            # If we reached the target node, return the accumulated weight
            if u == n - 1:
                return d
                
            if d > dist[u][cur]:
                continue
                
            for v, w in g[u]:
                # Determine the next consecutive count of identical labels
                if labels[v] != labels[u]:
                    nxt = 1
                else:
                    nxt = cur + 1
                    
                nd = d + w
                
                # Check if the transition is valid and provides a shorter path
                if nxt <= k and nd < dist[v][nxt]:
                    dist[v][nxt] = nd
                    heapq.heappush(pq, (nd, v, nxt))
                    
        return -1

import sys

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        sys.setrecursionlimit(200000)
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Determine appropriate LOG size for binary lifting
        LOG = 16
        while (1 << LOG) <= n:
            LOG += 1
            
        up = [[-1] * LOG for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        P = [0] * n
        
        # DFS to compute pre-order times, depths, binary lifting table, and initial root-to-node XOR sums
        timer = 0
        def dfs(u, p, d, current_p):
            nonlocal timer
            timer += 1
            tin[u] = timer
            depth[u] = d
            up[u][0] = p
            for j in range(1, LOG):
                if up[u][j-1] != -1:
                    up[u][j] = up[up[u][j-1]][j-1]
            
            char_mask = 1 << (ord(s[u]) - ord('a'))
            P[u] = current_p ^ char_mask
            
            tout[u] = tin[u]
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1, P[u])
                    tout[u] = max(tout[u], tout[v])
                    
        dfs(0, -1, 0, 0)
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for j in range(LOG - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != -1 and up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]
            
        # Build A array where A[tin[u]] = P[u]
        A = [0] * (n + 1)
        for u in range(n):
            A[tin[u]] = P[u]
            
        # Build difference array D for range XOR updates
        D = [0] * (n + 2)
        for i in range(1, n + 1):
            D[i] = A[i] ^ A[i - 1]
            
        # Initialize Fenwick tree
        fenwick = [0] * (n + 2)
        
        def fenwick_add(idx, val):
            while idx < len(fenwick):
                fenwick[idx] ^= val
                idx += idx & (-idx)
                
        def fenwick_query(idx):
            res = 0
            while idx > 0:
                res ^= fenwick[idx]
                idx -= idx & (-idx)
            return res
            
        for i in range(1, n + 1):
            fenwick_add(i, D[i])
            
        node_chars = list(s)
        ans = []
        
        for q in queries:
            parts = q.split()
            if parts[0] == "query":
                u = int(parts[1])
                v = int(parts[2])
                l = get_lca(u, v)
                pu = fenwick_query(tin[u])
                pv = fenwick_query(tin[v])
                lca_mask = 1 << (ord(node_chars[l]) - ord('a'))
                path_xor = pu ^ pv ^ lca_mask
                ans.append(bin(path_xor).count('1') <= 1)
            else:
                u = int(parts[1])
                new_c = parts[2]
                old_c = node_chars[u]
                if old_c != new_c:
                    old_mask = 1 << (ord(old_c) - ord('a'))
                    new_mask = 1 << (ord(new_c) - ord('a'))
                    delta = old_mask ^ new_mask
                    node_chars[u] = new_c
                    fenwick_add(tin[u], delta)
                    if tout[u] + 1 <= n + 1:
                        fenwick_add(tout[u] + 1, delta)
                        
        return ans

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Initialize the grid filled with obstacles '#'
        g = [["#"] * n for _ in range(m)]
        
        # Open the entire first row
        g[0] = ["."] * n
        
        # Open the entire last column
        for i in range(m):
            g[i][-1] = "."
            
        # Convert rows to strings and return
        return ["".join(row) for row in g]
        

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If there's only 1 row or the string fits entirely in the rows
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of lists to hold characters for each row
        rows = [[] for _ in range(numRows)]
        current_row = 0
        step = 1  # 1 means moving down, -1 means moving up
        
        for char in s:
            rows[current_row].append(char)
            
            # Reverse direction when hitting the top or bottom row
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
                
            current_row += step
            
        # Combine all rows into the final string
        return "".join("".join(row) for row in rows)

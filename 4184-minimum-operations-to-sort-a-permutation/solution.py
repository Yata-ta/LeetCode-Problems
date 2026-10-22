class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        
        def check(step: int) -> bool:
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n
                if nums[prev] > nums[curr]:
                    return False
            return True

        ans = float('inf')
        
        # Check if elements are increasing in the right direction from 0
        if check(1):
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)
            
        # Check if elements are increasing in the left direction from 0
        if check(-1):
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)
            
        return ans if ans != float('inf') else -1
        

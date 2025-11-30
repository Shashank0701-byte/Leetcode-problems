class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p
        if rem == 0:
            return 0
        
        prefix = 0
        seen = {0: -1}
        best = len(nums)
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            
            need = (prefix - rem) % p
            if need in seen:
                best = min(best, i - seen[need])
            
            seen[prefix] = i
        
        return best if best < len(nums) else -1

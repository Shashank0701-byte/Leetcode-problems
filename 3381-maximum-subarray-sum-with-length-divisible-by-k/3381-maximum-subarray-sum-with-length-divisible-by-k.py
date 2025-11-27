class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prefix = 0
        best = -10**18
        min_pref = [10**18] * k
        min_pref[0] = 0

        for i, num in enumerate(nums):
            prefix += num
            r = (i + 1) % k
            
            best = max(best, prefix - min_pref[r])
            min_pref[r] = min(min_pref[r], prefix)
        
        return best
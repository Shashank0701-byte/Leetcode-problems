class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0:1}
        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            ans += count.get(prefix-goal, 0)
            count[prefix] = count.get(prefix, 0) + 1
        
        return ans
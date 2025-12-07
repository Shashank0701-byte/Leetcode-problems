class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [x % 2 for x in nums]
        prefix = 0
        count = {0:1}
        ans = 0

        for x in nums:
            prefix += x

            if prefix - k in count:
                ans += count[prefix - k]
            
            count[prefix] = count.get(prefix, 0) + 1
        
        return ans

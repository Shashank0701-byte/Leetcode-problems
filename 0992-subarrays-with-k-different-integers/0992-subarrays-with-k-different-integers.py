class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(K):
            count = {}
            l = 0
            ans = 0
            for r, x in enumerate(nums):
                count[x] = count.get(x, 0) + 1
                
                while len(count) > K:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                
                ans += r - l + 1
            
            return ans
        
        return atMost(k) - atMost(k - 1)
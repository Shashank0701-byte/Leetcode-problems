class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        prev = 0

        for bit in nums:
            prev = (prev*2 + bit) % 5
            ans.append(prev == 0)
        
        return ans
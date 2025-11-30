class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        unique = sorted(freq.keys(), reverse=True)
        
        greater = 0
        ans = 0
        
        for val in unique:
            if greater >= k:
                ans += freq[val]
            greater += freq[val]
        
        return ans
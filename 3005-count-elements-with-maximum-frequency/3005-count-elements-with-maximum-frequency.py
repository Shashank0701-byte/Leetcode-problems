class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxf = max(freq.values())
        return sum(v for v in freq.values() if v == maxf)
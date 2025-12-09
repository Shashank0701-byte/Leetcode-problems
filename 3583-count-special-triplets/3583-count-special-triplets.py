class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        r = Counter(nums)
        l = Counter()

        ans = 0

        for j in range(n):
            r[nums[j]] -= 1
            need = nums[j]*2

            l_count = l[need]
            r_count = r[need]

            ans = (ans + l_count * r_count) % MOD
            l[nums[j]] += 1
        
        return ans
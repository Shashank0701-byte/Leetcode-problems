class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def is_strictly_increasing(subarr):
            return all(subarr[i] < subarr[i+1] for i in range(len(subarr)-1))

        n = len(nums)
        for a in range(n - 2 * k + 1):
            sub1 = nums[a:a+k]
            sub2 = nums[a+k:a+2*k]
            if is_strictly_increasing(sub1) and is_strictly_increasing(sub2):
                return True
        return False
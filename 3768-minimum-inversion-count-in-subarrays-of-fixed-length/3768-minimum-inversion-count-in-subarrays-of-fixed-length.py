class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sl = []  
        inv_count = 0
        ans = float('inf')

        for i in range(n):
            if i - k >= 0:
                out = nums[i - k]
                smaller = bisect_left(sl, (out, 0))
                inv_count -= smaller
                pos = bisect_left(sl, (out, i - k))
                if pos < len(sl) and sl[pos] == (out, i - k):
                    sl.pop(pos)

            in_val = nums[i]
            greater = len(sl) - bisect_right(sl, (in_val, 10**18))
            inv_count += greater
            pos = bisect_right(sl, (in_val, i))
            sl.insert(pos, (in_val, i))

            if i >= k - 1:
                ans = min(ans, inv_count)

        return ans
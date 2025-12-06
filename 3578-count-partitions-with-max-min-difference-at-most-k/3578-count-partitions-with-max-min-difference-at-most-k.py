class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * n
        pref = [0] * n 

        maxD = deque()
        minD = deque()

        left = 0

        for i in range(n):
            while maxD and maxD[-1] < nums[i]:
                maxD.pop()
            maxD.append(nums[i])

            while minD and minD[-1] > nums[i]:
                minD.pop()
            minD.append(nums[i])
            while maxD[0] - minD[0] > k:
                if maxD[0] == nums[left]:
                    maxD.popleft()
                if minD[0] == nums[left]:
                    minD.popleft()
                left += 1
            if left == 0:
                dp[i] = (1 + (pref[i-1] if i > 0 else 0)) % MOD
            else:
                dp[i] = (pref[i-1] - pref[left-2]) % MOD if left > 1 else pref[i-1] % MOD
            pref[i] = (dp[i] + (pref[i-1] if i > 0 else 0)) % MOD

        return dp[n-1]
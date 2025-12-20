class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        ans = 0
        for c in range(n):
            for r in range(m - 1):
                if strs[r][c] > strs[r + 1][c]:
                    ans += 1
                    break
        return ans
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        base = sum(prices[i] * strategy[i] for i in range(n))

        win = k // 2 
        pref_sp = [0]
        for i in range(n):
            pref_sp.append(pref_sp[-1] + prices[i] * strategy[i])
        pref_p = [0]
        for x in prices:
            pref_p.append(pref_p[-1] + x)

        best_gain = 0

        for i in range(n - k + 1):
            mid = i + win
            end = i + k

            removed = pref_sp[end] - pref_sp[i]
            added = pref_p[end] - pref_p[mid]

            gain = added - removed
            best_gain = max(best_gain, gain)

        return base + best_gain

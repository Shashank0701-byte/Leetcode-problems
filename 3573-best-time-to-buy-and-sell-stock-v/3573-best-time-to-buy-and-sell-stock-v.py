class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        NEG = -10**18

        dp = [[[NEG] * (k + 1) for _ in range(3)] for _ in range(n + 1)]

        for t in range(k + 1):
            dp[n][0][t] = 0

        for i in range(n - 1, -1, -1):
            for t in range(k + 1):
                dp[i][0][t] = max(
                    dp[i + 1][0][t],
                    -prices[i] + dp[i + 1][1][t],
                    prices[i] + dp[i + 1][2][t]
                )

                if t < k:
                    dp[i][1][t] = max(
                        dp[i + 1][1][t],
                        prices[i] + dp[i + 1][0][t + 1]
                    )
                    dp[i][2][t] = max(
                        dp[i + 1][2][t],
                        -prices[i] + dp[i + 1][0][t + 1]
                    )

        return dp[0][0][0]
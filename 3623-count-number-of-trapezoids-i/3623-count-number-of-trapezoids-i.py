class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7      
        y_count = defaultdict(int)
        for x, y in points:
            y_count[y] += 1

        pairs = []
        for y in y_count:
            c = y_count[y]
            if c >= 2:
                pairs.append(c * (c - 1) // 2)
        total = 0
        S = sum(pairs) % MOD

        for p in pairs:
            S = (S - p) % MOD
            total = (total + p * S) % MOD

        return total
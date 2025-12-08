class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                c = int((a*a + b*b) ** 0.5)
                if c <= n and c*c == a*a + b*b:
                    count += 1
        return count

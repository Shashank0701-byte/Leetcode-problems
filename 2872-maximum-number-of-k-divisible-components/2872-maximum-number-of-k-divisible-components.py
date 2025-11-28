class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        self.ans = 0

        def dfs(node, parent):
            subtotal = values[node]

            for child in g[node]:
                if child == parent:
                    continue
                subtotal += dfs(child, node)

            if subtotal % k == 0:
                self.ans += 1
                return 0
            return subtotal % k
        
        dfs(0, -1)
        return self.ans
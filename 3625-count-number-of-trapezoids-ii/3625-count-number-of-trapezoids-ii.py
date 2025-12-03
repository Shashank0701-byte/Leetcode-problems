class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(points)
        def slope(p, q):
            dx = q[0] - p[0]
            dy = q[1] - p[1]

            if dx == 0:
                return (1, 0), p[0] * 1 - p[1] * 0  
            if dy == 0:
                return (0, 1), p[0] * 0 - p[1] * 1  

            g = math.gcd(dx, dy)
            dx //= g
            dy //= g
            if dx < 0:            
                dx, dy = -dx, -dy
            lid = p[0] * dy - p[1] * dx
            return (dy, dx), lid

        edges = defaultdict(lambda: defaultdict(int))
        lines = defaultdict(set)

        for i in range(n):
            for j in range(i + 1, n):
                k, lid = slope(points[i], points[j])
                edges[k][lid] += 1
                lines[(k, lid)].add(i)
                lines[(k, lid)].add(j)

        if len(edges) == 1:
            return 0

        ans = 0
        for k, mp in edges.items():
            vals = list(mp.values())  
            m = len(vals)
            for i in range(m - 1):
                n1 = vals[i]
                for j in range(i + 1, m):
                    n2 = vals[j]
                    ans = (ans + n1 * n2) % MOD

        def count_parallelograms(pts: List[List[int]]) -> int:
            m = len(pts)
            if m < 4:
                return 0
            mid_count = defaultdict(int)
            for i in range(m):
                x1, y1 = pts[i]
                for j in range(i + 1, m):
                    x2, y2 = pts[j]
                    mx = x1 + x2
                    my = y1 + y2
                    mid_count[(mx, my)] += 1
            total = 0
            for cnt in mid_count.values():
                if cnt >= 2:
                    total += cnt * (cnt - 1) // 2
            return total

        dup = count_parallelograms(points)
        for (_, _), idxs in lines.items():
            if len(idxs) >= 4:
                sub_pts = [points[i] for i in idxs]
                dup -= count_parallelograms(sub_pts)

        return (ans - dup) % MOD

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)

        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()

        covered = 0

        for x, y in buildings:
            row = rows[x]
            col = cols[y]

            i = bisect.bisect_left(row, y)
            j = bisect.bisect_left(col, x)
            left = (i > 0)
            right = (i + 1 < len(row))
            up = (j > 0)
            down = (j + 1 < len(col))

            if left and right and up and down:
                covered += 1

        return covered
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        parent = list(range(n))
        size = [1] * n
        
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            size[pa] += size[pb]

        secret = {0, firstPerson}

        i = 0
        m = len(meetings)

        while i < m:
            t = meetings[i][2]
            batch = []
            while i < m and meetings[i][2] == t:
                x, y, _ = meetings[i]
                union(x, y)
                batch.append((x, y))
                i += 1

            comp = {}
            for x, y in batch:
                for p in (x, y):
                    rt = find(p)
                    if rt not in comp:
                        comp[rt] = set()
                    comp[rt].add(p)
            new_secret = set()
            for rt, group in comp.items():
                if any(p in secret for p in group):
                    new_secret |= group

            secret |= new_secret
            for rt, group in comp.items():
                if not any(p in secret for p in group):
                    for p in group:
                        parent[p] = p
                        size[p] = 1

        return list(secret)
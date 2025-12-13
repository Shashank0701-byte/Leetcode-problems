class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        cat_rank = {cat: i for i, cat in enumerate(valid_categories)}

        result = []
        for c, cat, active in zip(code, businessLine, isActive):
            if not c or any(not (ch.isalnum() or ch == "_") for ch in c):
                continue
            if cat not in cat_rank:
                continue
            if not active:
                continue
            result.append((cat_rank[cat], c))

        result.sort(key=lambda x: (x[0], x[1]))
        return [c for _, c in result]
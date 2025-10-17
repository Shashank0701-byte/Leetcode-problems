class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            total = 0
            required_days = 1
            for weight in weights:
                if total + weight > capacity:
                    required_days += 1
                    total = 0
                total += weight
            return required_days <= days
        
        l = max(weights)
        r = sum(weights)

        while(l<=r):
            mid = (l+r)//2
            if canShip(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
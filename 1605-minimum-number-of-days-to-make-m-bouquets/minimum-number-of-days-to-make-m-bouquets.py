class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if n < m * k:
            return -1
        
        def canMake(days):
            bouquets = flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        l = min(bloomDay)
        r = max(bloomDay)
        answer = -1
        while(l<=r):
            mid = (l+r)//2

            if canMake(mid):
                answer = mid
                r = mid - 1
            else:
                l = mid + 1
        return answer
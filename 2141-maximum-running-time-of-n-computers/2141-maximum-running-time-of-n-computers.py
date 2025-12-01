class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        left, right = 0, total // n
        
        def can_run(T):
            usable = 0
            for b in batteries:
                usable += min(b, T)
            return usable >= T * n
        
        while left < right:
            mid = (left + right + 1) // 2
            if can_run(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
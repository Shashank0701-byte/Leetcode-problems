class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        n = len(events)

        futureBest = [0]*n
        futureBest[-1] = events[-1][-1]

        for i in range(n-2, -1, -1):
            futureBest[i] = max(events[i][2], futureBest[i+1])
        starts = [event[0] for event in events]

        ans = 0
        for i in range(n):
            value = events[i][2]
            end_time = events[i][1]
            j = bisect.bisect_right(starts, end_time)


            if j < n:
                ans = max(ans, value + futureBest[j])
            else:
                ans = max(ans, value)
        
        return ans

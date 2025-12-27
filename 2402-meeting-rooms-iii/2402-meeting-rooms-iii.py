class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        busy_rooms = []
        count = [0] * n
        
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            duration = end - start
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (end_time + duration, room))
            
            count[room] += 1
        
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
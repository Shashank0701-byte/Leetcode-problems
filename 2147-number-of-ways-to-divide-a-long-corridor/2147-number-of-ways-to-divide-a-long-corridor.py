class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        seats = []
        for i, c in enumerate(corridor):
            if c == 'S':
                seats.append(i)

        if len(seats) == 0 or len(seats) % 2 == 1:
            return 0
        
        ways = 1
        for i in range(2, len(seats), 2):
            prev_end = seats[i - 1]    
            next_start = seats[i]      
            
            gap = next_start - prev_end
            ways = (ways * gap) % MOD
        
        return ways
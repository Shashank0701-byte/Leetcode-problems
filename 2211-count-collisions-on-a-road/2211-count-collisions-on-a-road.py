class Solution:
    def countCollisions(self, directions: str) -> int:
        s = directions.lstrip('L').rstrip('R')
        collisions = sum(c != 'S' for c in s)

        return collisions
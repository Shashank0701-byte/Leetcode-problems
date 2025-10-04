class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax=rmax=total = 0 
        l=0
        r=n-1

        while(l<r):
            if(height[l] <= height[r]):
                if(height[l] > lmax):
                    lmax = height[l]
                else:
                    total += lmax-height[l]
                    l = l+1
            else:
                if(height[r] > rmax):
                    rmax=height[r]
                else:
                    total += rmax-height[r]
                    r = r-1
        
        return total
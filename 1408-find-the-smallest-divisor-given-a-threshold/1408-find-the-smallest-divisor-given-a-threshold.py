class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        l=1
        h=max(nums)
        ans=0

        while(l<=h):
            mid=(l+h)//2
            total = sum((num+mid-1)//mid for num in nums)
            if(total <= threshold):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return l
        
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)

        while(l<r):
            mid=(l+r)//2

            cuts=1
            total=0

            for num in nums:
                if total+num > mid:
                    cuts+=1
                    total=0
                total+=num
            if cuts>k:
                l=mid+1
            else:
                r=mid
        return l
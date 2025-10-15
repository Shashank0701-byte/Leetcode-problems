class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while(l<r):
            mid = (l+r)//2

            if(nums[mid]>nums[r]):
                l = mid + 1
            else:
                r = mid
        return nums[l]
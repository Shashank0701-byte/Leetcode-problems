class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums,target):
            low, high = 0, len(nums) - 1
            first_pos = -1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    first_pos = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first_pos

        def find_last(nums,target):
            low,high=0, len(nums)-1
            last_pos = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last_pos = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else: 
                    high = mid - 1
            return last_pos
        
        first = find_first(nums, target)
        last = find_last(nums, target)

        return[first, last]

        
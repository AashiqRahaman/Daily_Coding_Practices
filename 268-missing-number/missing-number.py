class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        if nums[l-1]==l-1:
            return l
        for i in range(len(nums)):
            if nums[i]!=i:
                return nums[i]-1
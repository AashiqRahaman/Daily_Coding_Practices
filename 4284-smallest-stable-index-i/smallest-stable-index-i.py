class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = len(nums)
        for i in range(l):
            if max(nums[0:i+1])-min(nums[i:l])<=k:
                return i
        return -1

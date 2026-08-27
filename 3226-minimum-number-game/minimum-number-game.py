class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)-1):
            if i%2==0:
                temp = nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=temp
        return nums
        
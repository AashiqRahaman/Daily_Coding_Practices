class Solution:


    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        l = len(nums)
        temp= False
        for i in nums:
            xor = xor ^ i
            if i!=0:
                temp= True
        if xor!=0:
            return l
        else:
            if temp:
                return l-1
            else:
                return 0


class Solution:


    def longestSubsequence(self, nums: List[int]) -> int:
        l = len(nums)
        if [0]*(l)==nums:
            return 0
        xor = 0
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


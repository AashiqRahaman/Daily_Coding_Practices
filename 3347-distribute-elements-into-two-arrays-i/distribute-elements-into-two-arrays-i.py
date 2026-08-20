class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        p,q=0,0
        a=[]
        b=[]
        l= len(nums)
        if l<=2:
            return nums
        else:
            a.append(nums[0])
            b.append(nums[1])
            for i in range(2,l):
                if a[p]>b[q]:
                    a.append(nums[i])
                    p+=1
                else:
                    b.append(nums[i])
                    q+=1
        return a+b
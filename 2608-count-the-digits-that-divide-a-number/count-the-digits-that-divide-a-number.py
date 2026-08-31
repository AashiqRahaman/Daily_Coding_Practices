class Solution:
    def countDigits(self, num: int) -> int:
        a=[]
        temp=num
        while temp>0:
            t=temp%10
            a.append(t)
            temp=abs(temp//10)
        temp=0
        for i in a:
            if num%i==0:
                temp+=1

        return temp
        
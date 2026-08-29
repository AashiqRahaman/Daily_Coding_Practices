class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        s= sentences
        arr=[]
        m=0
        for i in range(len(s)):
            temp = s[i].split()
            m= max(m,len(temp))
        return m
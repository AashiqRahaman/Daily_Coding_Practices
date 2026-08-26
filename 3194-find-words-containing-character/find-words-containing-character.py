class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        op=[]
        for i in range(len(words)):
            if x in words[i]:
                op.append(i)
        return op
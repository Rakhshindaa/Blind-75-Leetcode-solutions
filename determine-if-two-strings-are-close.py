class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1=set(word1)
        w2=set(word2)
        if len(w1)!=len(w2):
            return False
        l1,l2=[],[]
        for i in w1:
            l1.append(word1.count(i))
            l2.append(word2.count(i))
        return sorted(l1)==sorted(l2)
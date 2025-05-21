class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        scount=tcount=0
        while scount<len(s) and tcount<len(t):
            if s[scount]==t[tcount]:
                scount=scount+1
            tcount=tcount+1
        return scount==len(s) 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=len(word1)
        n=len(word2)
        ans=''
        if m==n:
            for i in range(m):
                 ans=ans+word1[i]+word2[i]
        else:
            minlen=min(m,n)
            for i in range(minlen):
                ans=ans+word1[i]+word2[i]
            ans=ans+word1[minlen:]+word2[minlen:]
        return ans
        
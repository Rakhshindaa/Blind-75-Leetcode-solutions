class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        n=len(s)
        ls=[0]*n
        for i in range(n):
            if s[i] in vowels:
                ls[i]=1
        maxx=currmax=sum(ls[:k])
        for i in range(k,n):
            currmax=currmax+ls[i]-ls[i-k]
            maxx=max(maxx,currmax)
        return maxx
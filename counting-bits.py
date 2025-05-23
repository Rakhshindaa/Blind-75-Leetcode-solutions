class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        ans[0]=0
        for i in range(1,n+1):
            c=0
            k=i
            while  i!=0:
                if i&1==1:
                    c=c+1
                i=i>>1
            ans[k]=c
        return ans
        
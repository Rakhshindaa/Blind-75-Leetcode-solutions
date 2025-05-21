class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        if n==0:
            return 0
        w=0
        r=0
        while r<n:
            x=chars[r]
            count=0
            while r<n and chars[r]==x:
                count=count+1
                r=r+1
            chars[w]=x
            w=w+1
            if count>1:
                for c in str(count):
                    chars[w]=c
                    w=w+1
        return w
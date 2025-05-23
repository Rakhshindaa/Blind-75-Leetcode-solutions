class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count=0
        while c!=0 or b!=0 or a!=0:
            a_bit=a&1
            b_bit=b&1
            c_bit=c&1
            if c_bit==0:
                count=count+a_bit+b_bit
            elif a_bit==0 and b_bit==0:
                count+=1
            a=a>>1
            b=b>>1
            c=c>>1
        return count
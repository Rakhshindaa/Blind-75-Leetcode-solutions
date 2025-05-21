class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a=len(str1)
        b=len(str2)
        if str1+str2==str2+str1:
            while b%a!=0:
                a,b=b%a,a
            return str1[:a]
        return ''
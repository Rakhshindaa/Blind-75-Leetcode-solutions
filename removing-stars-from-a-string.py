class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for i in s:
            if i=='*':
                st.pop()
            else:
                st.append(i)
        ans=''
        for i in st:
            ans+=i
        return ''.join(ans)        
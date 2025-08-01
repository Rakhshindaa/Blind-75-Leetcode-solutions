class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            while st and i<0<st[-1]:
                if -i>st[-1]:
                    st.pop()
                    continue
                elif -i == st[-1]:
                    st.pop()
                break
            else:
                    st.append(i)
        return st
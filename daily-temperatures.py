class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for curr in range(n):
            while stack and temperatures[curr]>temperatures[stack[-1]]:
                prev=stack.pop()
                ans[prev]=curr - prev
            stack.append(curr)
        return ans
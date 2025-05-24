class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        rows=[]
        cols=[]
        for i in range(n):
            rows.append(grid[i])
            c=[]
            for k in range(n):
                c.append(grid[k][i])
            cols.append(c)
        cnt=0
        for i in rows:
            for j in cols:
                if i==j:
                    cnt=cnt+1
        return cnt
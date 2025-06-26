class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                    if i>0:
                        dp[i][j]=dp[i-1][j]+dp[i][j]
                    if j>0:
                        dp[i][j]=dp[i][j-1]+dp[i][j]
        return dp[m-1][n-1]

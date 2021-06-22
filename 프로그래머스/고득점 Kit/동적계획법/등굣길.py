mod = 1000000007
def solution(m, n, puddles):
    
    dp = [[0] * (m+1) for _ in range(n+1)]

    for c,r in puddles:
        dp[r][c] = -1
    
    for r in range(1,n+1):
        for c in range(1,m+1):
            
            if r == 1 and c == 1:
                dp[r][c] = 1
                continue
                
            if dp[r][c] == -1:
                continue
            
            if dp[r-1][c] != -1 and dp[r][c-1] != -1:
                dp[r][c] = (dp[r-1][c] + dp[r][c-1])%mod
            elif dp[r-1][c] != -1:
                dp[r][c] = dp[r-1][c] % mod
            elif dp[r][c-1] != -1:
                dp[r][c] = dp[r][c-1] % mod
            else:
                continue
                
    return dp[n][m]
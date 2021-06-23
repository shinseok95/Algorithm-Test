def solution(money):
    length = len(money)
    dp = [[0]*length for _ in range(2)]
    
    # 첫번째 집을 넣는 경우
    dp[0][0] = money[0]
    dp[0][1] = money[1]
    dp[0][2] = money[0] + money[2]
    
    # 첫번째 집을 넣지 않는 경우
    dp[1][1] = money[1]
    dp[1][2] = money[2]
    
    for i in range(3,length):
        dp[0][i] = max(dp[0][i-2],dp[0][i-3]) + money[i]
        dp[1][i] = max(dp[1][i-2],dp[1][i-3]) + money[i]
    
    return max(max(dp[0][length-4:length-1]),max(dp[1][length-3:]))
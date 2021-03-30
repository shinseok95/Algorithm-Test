"""
간단하게 메모이제이션으로 풀리는 문제다

다음 턴으로 넘길 때, 만약 다음 턴을 하는 사람이 지는 경우가 하나라도 있으면 해당 턴은 승리한다.

하지만, 다음 턴이 모두 이기는 경우라면 해당 턴은 패배한다.

1일 때, 패배
2일 때, 승리
3일 때, 패배
4일 때, 승리

를 breaking point로 설정하고 n-1, n-3, n-4로 dfs를 돌리면 된다.


"""

def dfs(n):

  if dp[n] != -1:
    return dp[n]
  
  # 0 승리 / 1 패배
  if n==1:
    dp[n] = 1
  elif n==2:
    dp[n] = 0
  elif n==3:
    dp[n] = 1
  elif n==4:
    dp[n] = 0
  else:

    n_1 = dfs(n-1)
    n_3 = dfs(n-3)
    n_4 = dfs(n-4)
    
    # 다음 턴으로 넘어갔을 때, 다음 턴이 모두 이기는 경우 -> 패배
    if n_1 == 0 and n_3 == 0 and n_4 == 0:
      dp[n] = 1
    # 다음 턴으로 넘어갔을 때, 다음 턴이 지는 경우가 있는 경우 -> 승리
    else:
      dp[n] = 0
    
  return dp[n]
    
N = int(input())
dp = [-1]*(1001)

result = dfs(N)

if result == 0:
  print('SK')
else:
  print('CY')
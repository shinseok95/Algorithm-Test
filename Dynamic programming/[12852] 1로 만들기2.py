"""
간단하게 풀린 문제다

N을 3으로 나누거나, 2로 나누거나, 1을 빼는 연산을 할 수 있을 때, 주어진 수를 1로 만드는 최소 연산 횟수를 구하는 문제였다.

이는 N에서 3가지 연산 중에 도출될 수 있는 수 중 가장 적은 연산횟수를 가지는 수의 연산횟수 +1을 하면 된다.

예를 들어, 10은 3으로 나눠지지 않기에 2로 나누거나 1을 빼야한다.
2로 나눈 5와 1을 뺀 9의 최소연산 횟수 중 더 작은 것에 1을 더하면 그것이 10의 최소 연산 횟수가 된다.

왜냐하면 이미 5와 9에 저장된 수는 최소 연산횟수를 보장하고 있기 때문이다.
"""

N = int(input())
dp = [0]*(N+1)
result = [N]
count = 0

for i in range(2,N+1):
  if i%3 == 0 and i%2 ==0:
    dp[i] = min(dp[i//3],dp[i//2],dp[i-1])+1
  elif i%3 ==0 and i%2 !=0:
    dp[i] = min(dp[i//3],dp[i-1])+1
  elif i%3 !=0 and i%2==0:
    dp[i] = min(dp[i//2],dp[i-1])+1
  else:
    dp[i] = dp[i-1]+1

count = dp[N]

while N != 1 :
  n = N

  if N%3==0:
    n = N//3

  if N%2==0:
    if dp[n] > dp[N//2]:
      n = N//2
  
  if dp[n] > dp[N-1]:
    n = N-1

  N = n

  result.append(N)

print(count)
print(*result)
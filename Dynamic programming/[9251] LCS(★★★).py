"""

DP문제인 것은 파악했는데, 결국 점화식을 세우진 못했다.

다른 사람의 풀이를 보니 새로운 방법으로 푸는 것을 발견했고, 다시 한번 부족함을 느꼈다..

풀이는 다음과 같다.

우선 2차원 리스트를 사용한다.

  a b c d e

0 0 0 0 0 0
a 1 1 1 1 1
c 1 1 2 2 2
d 1 1 2 3 3
c 1 1 2 3 3

그리고 각 col을 돌면서 두 문장을 비교한다.
예를 들어, r==2, c==2일 때는
abc와 ac를 비교한 값을 말하는 것이고 이때 r==2, c==3일때는 abcd와 ac를 비교하는 것이다.

이때 만약 row[r-1]와 col[c]의 문자가 같다면, 대각선 값에 +1을 해준다. 

예를 들어, r==2, c==2일 때 abc와 ac를 비교한 것으로 dp[2][2]=2 이다. 그리고 r==3,c==3은 abcd,acd이므로 둘다 같은 문자인 'd'가 붙었다.

즉, 그렇다면 대각선인 r==2,c==2인 것에 1을 더해주면 되는 것이다.

하지만 두 문자자가 다른 경우라면, dp[r-1][c] 또는 dp[r][c-1] 중 큰 값을 가져오면 된다.

예를 들어, r==3,c==2인 경우는 'd'와 'c'이므로 단어가 다르다.

그렇다면 dp[2][2] 또는 dp[3][1] 중 큰 값을 가져오면 되는데, 이것의 의미는
abc와 ac를 비교한 것과 ab와 acd를 비교한 것중에 더 큰 값을 가져오는 것이다.

이 경우에는 전자가 더 크므로, dp[3][2]는 2가 된다.

이런 방식을 점화식으로 하면 다음과 같아진다


dp[r][c] = max(dp[r-1][c], dp[r][c-1]) (단어가 다른 경우)
dp[r][c] = dp[r-1][c-1]+1 (단어가 같은 경우)


"""

import sys

second = list(sys.stdin.readline().rstrip())
first = list(sys.stdin.readline().rstrip())

first_len =len(first)
second_len = len(second)

dp = [[0]*second_len for _ in range(first_len+1)]

for i in range(1,first_len+1):
  for j in range(second_len):
    
    if first[i-1] == second[j]:
      if j == 0:
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j-1]+1
    else:
      if j == 0:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[first_len][second_len-1])


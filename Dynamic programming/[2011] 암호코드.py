"""

정답률 19%인 문제였는데, 다행이도 1시간 30분을 고민한 끝에 해결할 수 있었다.

우선 이 문제를 해결할 때 가장 중요한 아이디어는 뒤에서 한글자씩 왼쪽으로 옮겨가며 수를 세는 것이다.

예를 들어, 25114는 
4에서 1가지 경우의 수

14에서는 아무 것도 없을 때의 경우의수 , 4에서의 경우의 수

114에서는 4에서의 경우의 수 + 14에서의 경우의 수 

이런 식으로 진행할 수 있다.
즉, dp[i] = dp[i-1]+dp[i-2]이라는 점화식으로 표현될 수 있다는

하지만 1~26까지의 수로만 표현할 수 있다는 제약을 고려하는 것이 꽤나 까다롭다.

예를 들어, 만약 현재 수가 1,2가 아니면 두 자리 수를 만들 수 없기때문에, dp[i-2]의 경우의 수는 더할 필요가 없다

그러므로 점화식은 다음과 같아진다.

dp[i] = dp[i-1]+dp[i-2] (data[i]=1,2)
dp[i] = dp[i-1] (data[i]=3~9)

그러나 또한 제한이 있다.

i가 2인 경우에는 다음 수가 0~6인 경우만 dp[i-1]+dp[i-2]로 표현될 수 있다.

d[i] = dp[i-1]+dp[i-2] 
(data[i]=1 or (data[i]=2 and 0<=data[i-1]<=6)

dp[i] = dp[i-1] (else)

그러나 또 한가지의 제약사항이 있다.

만약 data[i]의 수가 0인 경우, 어떤 경우의 수도 존재하지 않는다.

왜냐하면 0은 1~26 범위에 존재하지 않기 때문이다.

이런 제약사항을 모두 고려하면 다음과 같은 점화식이 도출된다.

d[i] = 0 (data[i] = 0)

d[i] = dp[i-1]+dp[i-2] 
(data[i]=1 or (data[i]=2 and 0<=data[i-1]<=6)

dp[i] = dp[i-1] (else)
"""

import sys

mod = 1000000
N = list(sys.stdin.readline().rstrip())
length = len(N)

if length == 1:
  if N[0]=='0':
    print(0)
  else:
    print(1)
else:

  dp = [1,1]+[0]*(length-1)
  data = list(map(int,N))+[0]
  data.reverse()

  for i in range(1,length+1):

    if data[i] == 0 :
      dp[i] = 0
    elif data[i] == 1:
      dp[i] = (dp[i-1]+dp[i-2])%mod
    elif data[i] == 2:
      if 0<=data[i-1]<=6:
        dp[i] = (dp[i-1]+dp[i-2])%mod
      else:
        dp[i] = dp[i-1]%mod
    else:
      dp[i] = dp[i-1]%mod

  print(dp[length]%mod)
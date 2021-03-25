global dp

dp = [[[-99999]*101 for _ in range(101)] for _ in range(101)]

def w(a,b,c):
  
  A = a+50
  B = b+50
  C = c+50

  if dp[A][B][C] != -99999:
    return dp[A][B][C]
  
  if a<=0 or b<=0 or c <=0:
    dp[A][B][C] = 1
  
  elif a>20 or b>20 or c>20:    
    dp[A][B][C] = w(20,20,20)

  elif a<b<c:
    dp[A][B][C] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)

  else:
    dp[A][B][C] =  w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

  return dp[A][B][C]

while True:

  a,b,c = map(int,input().split())

  if a==-1 and b==-1 and c==-1:
    break
  else:
    ans = w(a,b,c)
    print("w({}, {}, {}) = {}".format(a,b,c,ans))
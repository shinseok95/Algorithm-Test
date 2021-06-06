import sys

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def dfs(visited,n,p,r,c):

  global N, result, prob

  if n == N:
    result += p
    return

  for i in range(4):
    next_r = r+dr[i]
    next_c = c+dc[i]

    if not visited[next_r][next_c]:
      visited[next_r][next_c] = True
      dfs(visited,n+1,p*prob[i],next_r,next_c)
      visited[next_r][next_c] = False

# E W S N
prob = list(map(int,sys.stdin.readline().split()))

N = prob[0]
del prob[0]

for i in range(4):
  prob[i] /= 100
result = 0

for i in range(4):
  visited = [[False]*((N*2)+1) for _ in range((N*2)+1)]

  visited[N][N] = True
   
  next_r = N+dr[i]
  next_c = N+dc[i]
  
  visited[next_r][next_c] = True

  dfs(visited,1,prob[i],next_r,next_c)

print(result)
#print('%.9f' % result)


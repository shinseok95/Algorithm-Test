import sys
sys.setrecursionlimit(10**5)

def dfs(r):

  if r == N:
    global result
    result += 1
    return

  for i in range(N):

    flag = True
    visited[r] = i
    
    for j in range(r):
      if visited[j] == i or abs(visited[j]-i) == r-j:
        flag = False
      
    if flag:
      dfs(r+1)

N = int(sys.stdin.readline())
result = 0 
visited = [0]*N

dfs(0)

sys.stdout.write(str(result))
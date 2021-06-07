import sys

INF = int(1e9)

def bf(start):
  
  dist[start] = 0
  
  for n in range(N):
    for m in range(1,M+1):
      
      s = bus[m][0]
      e = bus[m][1]
      d = bus[m][2]

      if dist[s] == INF:
        continue
      
      if dist[s]+d < dist[e]:
        dist[e] = dist[s]+d

        if n == N-1:
          return False
  
  return True

N,M = map(int,sys.stdin.readline().split())

dist = [INF] * (N+1)
bus = [(-1,-1,-1)]

for _ in range(M):
  s,e,d= map(int,sys.stdin.readline().split())
  bus.append((s,e,d))

if not bf(1):
  print(-1)
else:
  for i in range(2,N+1):
    if dist[i] == INF:
      print(-1)
    else:
      print(dist[i])

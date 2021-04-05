"""

이 문제는 서로소 집합을 통해 해결할 수 있었다.

우선 기지간의 거리를 계산(유클리드 거리법)하고 범위안에 들어오는 기지들간에는 연결되는 것으로 간주한다.

그리고 연결된 기지끼리 서로소 집합을 통해 서로 같은 통신망을 사용하는지 검사하면 된다.

여기서 꽤나 시간이 많이 걸린점은 마지막에 부모테이블을 최신화 해주지 않아서였다.

find_parent 함수에서 매번 최신화를 해주는 줄 알았는데, 아마 루트 노드만 최신화 해주고 자식 노드들은 최신화 해주지 않는 것 같다.

다음부터는 이런 유형의 문제가 나오면 무조건 부모 테이블을 최신화 하는 것을 잊으면 안될 것 같다.

"""

import sys
from math import sqrt

def find_parent(parent,x):
  
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])

  return parent[x]

def union_parent(parent,a,b):

  A = find_parent(parent,a)
  B = find_parent(parent,b)
  
  if A<B:
    parent[B] = A
  else:
    parent[A] = B

def cal_distance(x1,x2,y1,y2):

  x = (x1-x2)*(x1-x2)
  y = (y1-y2)*(y1-y2)
  z = sqrt(x+y)

  return z
  
T = int(sys.stdin.readline())
result = []

for _ in range(T):  
  N = int(sys.stdin.readline())
  graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
  parent = [0]*(N)

  for i in range(N):
    parent[i] = i

  for i in range(N):
    for j in range(i+1,N):
      
      dist = cal_distance(graph[i][0],graph[j][0],graph[i][1],graph[j][1])

      if dist <= graph[i][2]+graph[j][2] and parent[i] != parent[j]:
        union_parent(parent,i,j)
  
  for i in range(N):
    find_parent(parent,i)

  result.append(len(set(parent)))

for i in result:
  sys.stdout.write(str(i)+'\n')

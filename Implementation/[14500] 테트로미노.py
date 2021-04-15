"""
나는 단순히 모든 도형의 모양의 값을 비교하는 방식으로 풀었다.

왜냐하면, 보드가 N^2이므로 상수번 반복한다고해서 시간초과가 뜰 것 같진 않았기 때문이다.

다만, 여기서 주의해야할 점은 긴 막대기 형태와 정사각형 형태는 그냥 이중 for문을 돌려도 되지만, 다른 모양들은 다른 방식으로 접근해야한다

나는 우선 6개를 더한후, 그 중에서 조건에 맞도록 2개를 빼는 방식을 선택했다.

결과는 통과!

그러나 이 문제는 찾아보니 dfs와 백트래킹을 이용한 문제였다.

나도 처음에 dfs를 사용할 생각을 했으나, 만 ㅗ 형태의 도형을 어떻게 처리할지 잘 모르겠어서 전부 구해버렸다.

그러나 다른 풀이를 보니, 그냥 dfs를 돌리고, 모든 ㅗ모양들의 값을 구해서 그 중 더 큰 것을 반환하는 방식을 활용하였다.

다음에 다시 풀어볼 때는 이 방식을 사용해봐야할 것 같다.
"""

import sys

N,M = map(int,sys.stdin.readline().split())
graph = []
max_value = 0
hor_shape = []
hor_value = []

ver_shape = []
ver_value = []

for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

# 가로 일자형 도형
for i in range(N):
  for j in range(M-3):
    max_value = max(max_value,sum(graph[i][j:j+4]))

# 세로 일자형 도형
for i in range(N-3):
  for j in range(M):
    max_value = max(max_value,graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+3][j])

# 정사각형 도형
for i in range(N-1):
  for j in range(M-1):
    max_value = max(max_value,sum(graph[i][j:j+2])+sum(graph[i+1][j:j+2]))

# 6개 가로 도형
for i in range(N-1):
  for j in range(M-2):
    hor_value.append(sum(graph[i][j:j+3])+sum(graph[i+1][j:j+3]))

    shape = []
    for _i in range(2):
      for _j in range(3):
        shape.append(graph[i+_i][j+_j])
    hor_shape.append(shape)

# 6개 세로 도형
for i in range(N-2):
  for j in range(M-1):
    ver_value.append(sum(graph[i][j:j+2])+sum(graph[i+1][j:j+2])+sum(graph[i+2][j:j+2]))

    shape = []
    for _i in range(3):
      for _j in range(2):
        shape.append(graph[i+_i][j+_j])
    ver_shape.append(shape)


for i in range(len(hor_shape)):
  
  value = hor_shape[i][0]+hor_shape[i][1]

  value = min(value, hor_shape[i][0]+hor_shape[i][2])
  value = min(value,hor_shape[i][1]+hor_shape[i][2])
  value = min(value,hor_shape[i][0]+hor_shape[i][5])
  value = min(value,hor_shape[i][3]+hor_shape[i][4])
  value = min(value,hor_shape[i][3]+hor_shape[i][5])
  value = min(value,hor_shape[i][4]+hor_shape[i][5])
  value = min(value,hor_shape[i][3]+hor_shape[i][2])

  max_value = max(max_value,hor_value[i]-value)


for i in range(len(ver_shape)):
  
  value = ver_shape[i][0]+ver_shape[i][2]

  value = min(value, ver_shape[i][0]+ver_shape[i][4])
  value = min(value,ver_shape[i][2]+ver_shape[i][4])
  value = min(value,ver_shape[i][0]+ver_shape[i][5])
  value = min(value,ver_shape[i][1]+ver_shape[i][3])
  value = min(value,ver_shape[i][1]+ver_shape[i][5])
  value = min(value,ver_shape[i][3]+ver_shape[i][5])
  value = min(value,ver_shape[i][1]+ver_shape[i][4])

  max_value = max(max_value,ver_value[i]-value)

print(max_value)
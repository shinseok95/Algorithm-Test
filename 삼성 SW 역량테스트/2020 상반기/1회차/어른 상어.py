"""
21.07.05
삼성 SW 역량평가 2020년 상반기 기출문제 2-3
풀이 결과 : 정답
풀이 시간 : 2시간

너무 더럽게 풀어서 기분이 그닥 좋진 않다..
다음에 풀때는 좀 더 깔끔하게 풀어야겠다

그리고 이번 문제를 풀면서 느낀점은 삼성 코테는 시간복잡도를 그닥 신경 안써도 되는 것 같다

이렇게 더럽게 풀었는데도 시간초과가 뜨지 않는 거 보면, 어떻게 풀던 구현만 되면 시간 내에 돌아가도록 testcase를 주는 것 같다

"""

import sys
dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]

def move():

  global N,M,K,smell,sharks,sharks_dir,sharks_priority_dir

  cnt = 0

  # stel 1 : 냄새 제거

  for i in range(1,N+1):
    for j in range(1,N+1):
      if smell[i][j][0] > 0:
        smell[i][j][0] -= 1
  
  # step 2 : 상어 이동

  for i in range(M,0,-1):
    r = sharks[i][0]
    c = sharks[i][1]
    
    if r == -1 and c == -1:
      cnt += 1
      continue
    
    flag = True

    # 냄새가 없는 곳 탐색

    for j in range(1,5):
      next_r = r + dr[sharks_priority_dir[i][sharks_dir[i]][j]]
      next_c = c + dc[sharks_priority_dir[i][sharks_dir[i]][j]]

      if 0<next_r<=N and 0<next_c<=N:
        if smell[next_r][next_c][0]== 0 and smell[next_r][next_c][1] == 0:
          sharks_dir[i] = sharks_priority_dir[i][sharks_dir[i]][j]

          sharks[i][0] = next_r
          sharks[i][1] = next_c
          smell[next_r][next_c][0] = K
          smell[next_r][next_c][1] = i

          flag = False
          break
        elif smell[next_r][next_c][0] == K:
          sharks_dir[i] = sharks_priority_dir[i][sharks_dir[i]][j]

          sharks[smell[next_r][next_c][1]][0] = -1
          sharks[smell[next_r][next_c][1]][1] = -1
          
          sharks[i][0] = next_r
          sharks[i][1] = next_c

          smell[next_r][next_c][0] = K
          smell[next_r][next_c][1] = i

          flag = False
          break
    
    # 자기 냄새 탐색

    if flag:

      for j in range(1,5):

        next_r = r + dr[sharks_priority_dir[i][sharks_dir[i]][j]]
        next_c = c + dc[sharks_priority_dir[i][sharks_dir[i]][j]]

        if 0<next_r<=N and 0<next_c<=N:
          if smell[next_r][next_c][1] == i:
            graph[next_r][next_c] = i
            sharks_dir[i] = sharks_priority_dir[i][sharks_dir[i]][j]

            sharks[i][0] = next_r
            sharks[i][1] = next_c
            smell[next_r][next_c][0] = 1001
            smell[next_r][next_c][1] = i

            break
  
  # stel 3 : 임시로 저장한 냄새 정보 업데이트

  for i in range(1,N+1):
    for j in range(1,N+1):
      if smell[i][j][0] == 0 and smell[i][j][1] != 0:
        smell[i][j][1] = 0

      elif smell[i][j][0] == 1001 and smell[i][j][1] != 0:
        smell[i][j][0] = K

  if M-cnt == 1:
    return True
  else:
    return False

N,M,K = map(int,sys.stdin.readline().split())
graph = [[-1]*(N+1)]
smell = [[[0]*2 for _ in range(N+1)] for _ in range(N+1)]
sharks = [[] for _ in range(M+1)]

for i in range(1,N+1):
  graph.append([-1]+list(map(int,sys.stdin.readline().split())))

  for j in range(1,N+1):
    if graph[i][j] != 0:
      smell[i][j][0] = K
      smell[i][j][1] = graph[i][j]

      sharks[graph[i][j]].append(i)
      sharks[graph[i][j]].append(j)
  
sharks_dir = [-1]+list(map(int,sys.stdin.readline().split()))

sharks_priority_dir = [[[-1]*4 for _ in range(4)]]

for _ in range(M):
  shark = [[-1,-1,-1,-1]]
  
  for _ in range(4):
    shark.append([-1]+list(map(int,sys.stdin.readline().split())))
  sharks_priority_dir.append(shark)

answer = 0
while answer <= 1000:
  if move():
    print(answer)
    exit()

  answer += 1
print(-1)
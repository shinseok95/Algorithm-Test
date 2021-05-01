"""
21.05.01
삼성 SW 역량평가 2021년 기출문제 -1
풀이 결과 : 정답
풀이 시간 : 44분
"""

import sys

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def find_like(n):

  tmp_list = []

  for r in range(1,N+1):
    for c in range(1,N+1):

      if graph[r][c] != 0:
        continue
      
      friends_cnt = 0
      empty_cnt = 0

      for i in range(4):
        next_r = r+dr[i]
        next_c = c+dc[i]

        if 1<=next_r<=N and 1<=next_c<=N:
          if graph[next_r][next_c] == 0:
            empty_cnt+=1
          else:
            if like_list[n][0].count(graph[next_r][next_c]) == 1:

              friends_cnt += 1
        
      tmp_list.append((friends_cnt,empty_cnt,r,c))
  
  tmp_list.sort(key = lambda x : (-x[0],-x[1],x[2],x[3]))

  return tmp_list[0][2],tmp_list[0][3]

def cal_result():

  result = 0

  for r in range(1,N+1):
    for c in range(1,N+1):
      
      cnt = 0

      for i in range(4):
        next_r = r+dr[i]
        next_c = c+dc[i]
        
        if 1<=next_r<=N and 1<=next_c<=N:
          if like_list[graph[r][c]][0].count(graph[next_r][next_c]) == 1:
            cnt+=1

      if cnt > 0:
        result += 10**(cnt-1)
  
  return result

N = int(sys.stdin.readline())
graph = [[0]*(N+1) for _ in range(N+1)]
students = [0]
like_list = [[] for _ in range((N*N)+1)]

for _ in range(N*N):
  student, l1,l2,l3,l4 = map(int,sys.stdin.readline().split())

  students.append(student)
  like_list[student].append((l1,l2,l3,l4))

for n in students:
  if n == 0:
    continue

  r,c = find_like(n)
  graph[r][c] = n

print(cal_result())
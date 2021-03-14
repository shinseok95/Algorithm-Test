from collections import deque

def bfs(graph,home_x,home_y,festival_x,festival_y):

  queue = deque([(home_x,home_y)])

  while queue:
    x,y = queue.popleft()

    if 0<=abs(festival_x-x)+abs(festival_y-y) <=1000:
      global result

      result = True
      break

    tmp_graph = graph[:]

    for to_x,to_y in tmp_graph:

      if 0<=abs(to_x-x)+abs(to_y-y)<=1000:
        queue.append((to_x,to_y))
        graph.remove((to_x,to_y))

T = int(input())

for _ in range(T):
  N = int(input())

  home_x, home_y = map(int,input().split())

  graph = []
  visited = [False]*N
  result = False

  for _ in range(N):
    mart_x, mart_y = map(int,input().split())

    graph.append((mart_x,mart_y))

  festival_x, festival_y = map(int,input().split())

  bfs(graph,home_x,home_y,festival_x,festival_y)

  if result:
    print('happy')
  else:
    print('sad')
from collections import deque

def bfs(graph,visited,i):
    
    if visited[i]:
        return 0
    
    q = deque()
    q.append(i)
    visited[i] = True
    
    while q:
        n = q.popleft()
        
        for m in graph[n]:
            if not visited[m]:
                visited[m] = True
                q.append(m)
    
    return 1
    
def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(n)]
    visited = [False] * n
    
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    for i in range(n):
        answer += bfs(graph,visited,i)
    
    return answer
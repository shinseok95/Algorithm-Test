from heapq import heappush, heappop
INF = int(1e9)

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)
    q = []
    
    for start,end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    heappush(q,(0,1))
    distance[1] = 0
    
    while q:
        dist, now = heappop(q)
        
        if distance[now] < dist:
            continue
        
        for node in graph[now]:
            cost = dist+1
            if cost < distance[node]:
                distance[node] = cost
                heappush(q,(cost,node))
    
    return distance.count(max(distance[1:]))
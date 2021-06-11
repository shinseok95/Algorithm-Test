"""
이 문제가 어려웠던 것은 기존의 문제들은 각 노드가 숫자 또는 그래프로 주어졌다면, 이 문제는 각 노드가 문자열로 주어졌다는 점이었다.

그래서 각 노드들을 통해 그래프를 만들기 위해(visited 또한), hash를 썼다.

그리고 출력 또한, 경로를 만들어줘야 했는데, 사실 백준에서는 경로를 직접 반환하는 경우의 문제는 거의 없었다. 
(대부분 개수 문제)

그래서 경로를 반환하는데도 꽤나 어려움이 있었다. 결국 경로를 dfs의 반환 값을 queue로 줘서
"""

from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(flights,visited,cnt,depart,length):
    
    if cnt == length:
        q = deque()
        q.append(depart)
        return q
    
    if flights.get(depart) == None:
        return None
    
    for i in range(len(flights[depart])):
        if not visited[depart][i]:
            visited[depart][i] = True
            
            res = dfs(flights,visited,cnt+1,flights[depart][i],length)
            
            if res == None:
                visited[depart][i] = False
                continue
            else:
                res.appendleft(depart)
                return res
    
    return None

def solution(tickets):
    
    flights = dict()
    visited = dict()
    
    for ticket in tickets:
        if flights.get(ticket[0]) == None:
            flights[ticket[0]] = [ticket[1]]
        else:
            flights[ticket[0]].append(ticket[1])
    
    for flight in flights.keys():
        flights[flight].sort()
        visited[flight] = [False] * len(flights[flight])
    
    answer = dfs(flights,visited,0,"ICN",len(tickets))
    return list(answer)
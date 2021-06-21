from collections import deque 

def solution(routes):
    routes.sort(key = lambda x : (x[1],x[0]))
    q = deque(routes)
    answer = 0
    
    while q:
        answer += 1
        left, right = q.popleft()
        
        while q:
            n_left,n_right = q.popleft()
            
            if n_left > right:
                q.appendleft([n_left,n_right])
                break
        
    return answer
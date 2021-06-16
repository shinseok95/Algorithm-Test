from collections import deque

def solution(progresses, speeds):
    
    answer = []
    p = deque(progresses)
    s = deque(speeds)
    
    while p :
        p = deque([x+y for x,y in zip(p,s)])
        
        cnt = 0
        
        for i in range(len(p)):
            if p[i] >= 100:
                cnt += 1
            else:
                break
        
        if cnt > 0 :
            for i in range(cnt):
                p.popleft()
                s.popleft()
            answer.append(cnt)
        
    return answer
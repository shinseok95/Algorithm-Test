from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    cnt_list = [0] * 10
    
    for i in range(len(priorities)):
        cnt_list[priorities[i]] += 1
        q.append((priorities[i],i))
    
    for i in range(9,-1,-1):
        if cnt_list[i] == 0:
            continue
        
        for j in range(len(q)):
            if cnt_list[i] == 0:
                break
            p,k = q.popleft()
            
            if p == i:
                answer += 1
                if location == k:
                    return answer
                else :
                    cnt_list[i] -= 1
            else:
                q.append((p,k))
    
    return answer
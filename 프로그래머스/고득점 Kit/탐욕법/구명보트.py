from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    
    while people:
        answer += 1
        boat = limit
        
        while people:
            p = people.pop()
            
            if p <= boat:
                boat -= p
            else:
                people.append(p)
                break
        
        while people:
            p = people.popleft()
            
            if p <= boat:
                boat -= p
            else:
                people.appendleft(p)
                break
            
    return answer
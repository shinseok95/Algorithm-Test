def solution(n, lost, reserve):
    
    students = [ 0 if i == 0 or i == n+1 else 1 for i in range(n+2)]
    intersect = set(reserve) & set(lost)
    reserve = list(set(reserve) - intersect)
    lost = list(set(lost)-intersect)
    
    lost.sort()
    answer = 0
    
    for i in reserve:
        students[i] += 1
    
    for i in lost:
        if students[i-1] > 1:
            students[i-1] -= 1
        elif students[i+1] > 1:
            students[i+1] -= 1
        else:
            students[i] -= 1
    
    for i in range(1,n+1):
        if students[i] > 0 :
            answer += 1
    return answer
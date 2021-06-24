"""
mid를 최댓값으로 생각하고
target을 제거한 돌의 개수라는 것까지는 생각해냈다

그런데 돌을 제거하는 방식을 제대로 생각해내지 못했다.

그리고 rock_cnt <= n의 경우 중에 가장 큰 경우를 구하는 것도 생각해내지 못했다..

어렵구나..
"""

def parametric(rocks,n):
    
    start = 1
    end = rocks[-1]
    result = 0 
    
    while start<=end:
        
        mid = (start+end)//2
        rock_cnt = 0
        prev = 0
        
        for now in range(1,len(rocks)):
            if rocks[now] - rocks[prev] < mid:
                rock_cnt += 1
            else:
                prev = now
        
        # rocn_cnt <= n인 경우에는 거리의 최솟값이 됨
        # 생각해보면, 최솟값 중 최댓값을 구한다는 건, 정답보다 작은 경우에서 정답을 찾아야하는 것

        if rock_cnt <= n :
            start = mid+1
            result = max(result,mid)
        else:
            end = mid - 1
            
    return result

def solution(distance, rocks, n):
    
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    return parametric(rocks,n)
from heapq import heappush, heappop

def solution(scoville, K):
    
    cnt = 0 
    scoville.sort()
    
    while len(scoville) > 1:
        
        first = heappop(scoville)
        second = heappop(scoville)
        
        if first >= K:
            return cnt
        else:
            heappush(scoville,(first+(second*2)))
            cnt += 1
                
    if scoville[0] >= K:
        return cnt
    else:
        return -1
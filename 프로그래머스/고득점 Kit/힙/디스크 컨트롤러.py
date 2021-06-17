from heapq import heappush, heappop
from collections import deque
import math

def solution(jobs):

    total_response_time = 0
    remain_time = 0
    time = 0
    cnt = len(jobs)

    jobs = deque(sorted(jobs,key = lambda x : (x[0],x[1])))
    q = []

    while q or jobs:

        if remain_time > 0:
            remain_time -= 1
            time += 1
            continue

        while jobs:
            s,t = jobs.popleft()

            if s<=time:
                heappush(q,[t,s])
            else:
                jobs.appendleft([s,t])
                break

        if len(q) > 0 :  
            t,s = heappop(q)
            remain_time = t-1
            total_response_time += ((time-s)+t)

        time += 1

    return math.floor(total_response_time/cnt)
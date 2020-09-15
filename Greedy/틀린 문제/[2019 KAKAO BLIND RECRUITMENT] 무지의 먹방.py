"""
https://programmers.co.kr/learn/courses/30/lessons/42891

처음으로 Priority Queue를 활용하는 문제를 풀게되었다.

처음에는 while문을 통해 전체 경우의 수를 계산하였는데, 효율성 테스트에서 시간초과가 나와 결국 답을 볼 수 밖에 없었다.

정답의 아이디어는 다음과 같다.

1. 데이터를 priority queue에 튜플로 넣음으로써, 자동으로 index도 보존하고 time도 sort한다.
2. 가장 적은 시간이 걸리는 음식을 먼저 제거함으로써 그리디하게 접근한다.
3. 음식을 제거할 수 있는 시간이 나오지 않는 경우 while문에서 빠져나온다.
4. 이후, queue에서 index 기준으로 정렬하고, 정답을 골라낸다.

단순히 답을 풀려고 하지 않고 어떻게하면 효율적으로 접근할 지 생각해내는 것이 중요한 것 같다.
또한, 생각해낸다면 이를 구현할 수 있도록 문법 또한 잘 익혀놔야할 것 같다.

"""
import heapq

def solution(food_times, k):
    
    if sum(food_times)<=k:
        return -1
    
    q = list()
    
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    sum_value = 0
    prev =0
    length = len(food_times)
    
    while (sum_value + (q[0][0]-prev)*length)<=k:t
        now = heapq.heappop(q)[0]
        sum_value += (now-prev)*length
        length -= 1
        prev = now
        
    result = sorted(q,key = lambda x: x[1])
    return result[(k-sum_value)%length][1]
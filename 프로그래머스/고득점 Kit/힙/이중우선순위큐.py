from heapq import heappush, heappop

def translate(operation):
    if operation[0] == 'I':
        return int(operation[2:])
    else:
        if operation[2] == '1':
            return 'max'
        else:
            return 'min'

def solution(operations):
    
    cnt = 0
    
    max_q = []
    min_q = []
        
    for operation in operations:

        data = translate(operation)
        
        if data == 'max':
            if cnt > 0:
                heappop(max_q)
                cnt -= 1
                
        elif data == 'min':
            if cnt > 0:
                heappop(min_q)
                cnt -= 1
        
        else:
            cnt += 1
            heappush(max_q,(data * -1))
            heappush(min_q,data)
    
    if cnt == 0:
        return [0,0]
    else:
        max_set = set(list(map(lambda x : x*-1,max_q)))
        min_set = set(min_q)
        total_set = sorted(max_set & min_set)
        
        return [total_set[-1],total_set[0]]
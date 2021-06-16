from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    w = 0
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    
    while truck or w > 0 :
        
        time += 1
        b = bridge.popleft()
        w -= b
        
        if len(truck) > 0 :
            if truck[0] + w <= weight:
                t = truck.popleft()
                w += t
                bridge.append(t)
            else:
                bridge.append(0)
        
    return time
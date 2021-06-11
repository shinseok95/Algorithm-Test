from bisect import bisect_left, bisect_right

def solution(citations):
    
    citations.sort()
    length = len(citations)
    h_index = 0
    
    for i in range(length+1):
        if length-bisect_left(citations,i) >= i:
            h_index = max(h_index,i)
    
    return h_index
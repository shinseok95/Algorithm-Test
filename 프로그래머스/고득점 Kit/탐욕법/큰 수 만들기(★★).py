"""
생각 해내는 것도 어려웠지만, 최적화가 미친 문제였다..

최적화를 열심히 해야겠다...
"""

array = None

def find_max_index(left,right):
    
    idx = left
    max_val = '1'
    
    for i in range(left,right+1):
        if array[i] == '9':
            return i
        elif array[i] > max_val:
            idx = i
            max_val = array[i]
            
    return idx

def solution(number, k):
    
    global array
    array = number
    cnt = k
    last_idx = 0
    length = len(number)
    answer=[]
    
    while cnt > 0:
        
        idx = find_max_index(last_idx,last_idx + cnt)
        answer.append(number[idx])
        cnt -= (idx-last_idx)
        last_idx = idx + 1
        
        if (length-last_idx) <= cnt:
            return ''.join(answer)
    
    return ''.join(answer) + number[last_idx:]
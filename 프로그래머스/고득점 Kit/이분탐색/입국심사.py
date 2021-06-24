def parametric(times,n):
    
    start = 0
    end = n*times[-1]
    result = 0
    
    while start<=end:
        mid = (start+end)//2
        mans = 0
        
        for time in times:
            mans += (mid//time)
            
        if mans < n:
            start = mid+1
        else:
            end = mid-1
            result = mid
    
    return result

def solution(n, times):
    
    times.sort()
    
    return parametric(times,n)
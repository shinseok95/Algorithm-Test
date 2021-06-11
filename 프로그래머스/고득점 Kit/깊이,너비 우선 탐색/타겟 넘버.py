def dfs(numbers, result,i,target):
    
    ans = 0
    
    if i == len(numbers)-1:
        
        if result+numbers[i] == target:
            ans += 1
        if result+(numbers[i]*-1) == target:
            ans += 1
        
        return ans
    
    ans += dfs(numbers,result+numbers[i],i+1,target)
    ans += dfs(numbers,(result+numbers[i]*-1),i+1,target)
    
    return ans

def solution(numbers, target):
    
    answer = 0
    
    answer += dfs(numbers,numbers[0],1,target)
    answer += dfs(numbers,(numbers[0]*-1),1,target)
        
    return answer
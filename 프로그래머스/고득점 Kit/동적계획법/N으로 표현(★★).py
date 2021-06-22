"""
처음에는 
n은 n-1에서 사칙연산 해주는 방식으로 풀었다.

그런데 계속 오답이 나와서 다른 사람의 질문을 확인하니, 

다른 경우의 수도 많았다.

예를 들어,
N = 4인 경우, (1,3),(2,2)가 있다.


"""

def solution(N, number):
    
    dp = [[] for _ in range(9)]
    
    # N 등장 횟수 (1~8)
    for i in range(1,9):
        
        # 5, 55, 555, 5555 등 체크
        tmp = 0
        for j in range(1,i+1):
            tmp*=10
            tmp+=N
            
        dp[i].append(tmp)
            
        for j in range(1,i):
            for left in dp[j]:
                for right in dp[i-j]:
                    
                    dp[i].append(left+right)
                    dp[i].append(left-right)
                    dp[i].append(right-left)
                    
                    if right != 0:   
                        dp[i].append(left//right)
                    if left != 0:
                        dp[i].append(right//left)
                    dp[i].append(left*right)
                    
        dp[i] = set(dp[i])
        
        if number in dp[i]:
            return i
            
    return -1
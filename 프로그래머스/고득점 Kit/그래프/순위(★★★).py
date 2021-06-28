"""
플로이드 워셜을 사용해서 순위를 구하는 건 처음 알았다

잘 배워두자
"""

def solution(n, results):
    
    answer = 0
    graph = [['?'] * (n+1) for _ in range(n+1)]
    
    for start,end in results:
        graph[start][end] = 'win'
        graph[end][start] = 'lose'
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k] == 'win' and graph[k][j] == 'win':
                    graph[i][j] = 'win'
                    graph[j][i] = 'lose'
                
                elif graph[i][k] == 'lose' and graph[k][j] == 'lose':
                    graph[i][j] = 'lose'
                    graph[j][i] = 'win'
    
    for i in range(1,n+1):
        if graph[i][1:].count('?') == 1:
            answer+=1
            
    return answer
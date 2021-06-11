"""
DFS 문제 중에서 처음 보는 형식이라서 적잖게 당황했던 것 같다.

우선 단어를 하나씩만 바꾸면서, 최종 목표 단어를 만들어야한다.

그렇기 위해서, 비교 대상 두 단어의 차이가 1개인지 확인하고, 이미 비교했던 단어인지 확인한다음 백트래킹을 통해서 모든 경우의 수를 탐색하도록 한다.

"""

import sys
sys.setrecursionlimit(10**5)

def comp(w1,w2):
    cnt = 0
    
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    
    return cnt

def dfs(begin,target,words,visited,i):
    
    if comp(begin,target) == 0:
        return i
    
    min_res = int(1e9)
    
    for word in words:
        if not visited[word]:
            if comp(begin,word) == 1:
                visited[word] = True
                min_res = min(min_res,dfs(word,target,words,visited,i+1))
                visited[word] = False
    
    return min_res
    
def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    visited = dict()
    
    for word in words:
        visited[word] = False
    
    answer = dfs(begin,target,words,visited,0)
    
    return answer
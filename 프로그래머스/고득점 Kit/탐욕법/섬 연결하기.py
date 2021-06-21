"""
최소 신장 트리
"""

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    
    p_a = find(parent,a)
    p_b = find(parent,b)
    
    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b
    

def solution(n, costs):
    costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    answer = 0
    
    for a,b,cost in costs:
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            answer += cost
    
    return answer
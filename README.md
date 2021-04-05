# Algorithm-Test-Exercise
> 코딩테스트를 대비한 문제 풀이를 정리하는 Repository입니다.

## 코딩테스트를 위한 파이썬

### 시간 복잡도
- 1초에 1000-2000만번 연산 가능
- N의 범위
  - 500 : O(N^3)
  - 2000 : O(N^2)
  - 100,000 : O(NlogN)
  - 10,000,000 : O(N)
 
### 데이터 수와 breaking point를 정해주지 않을 때

```python

while True:
    try: 
      n = int(input())
      
      # 여기서 계산하고 출력
      
    except:
      break 
```

```python

import sys

N = list(map(int, stdin.read().split()))

for n in N:
  # 여기서 계산하고 출력
```

### 재귀 깊이 조절

```python

import sys
sys.setrecursionlimit(10^5)
```

### Python3와 Pypy3 비교 

- Python3 
  - 장점 : 메모리 사용량이 적음
  - 단점 : 느림 => Pypy3이 사용 가능하다면 Pypy3를 사용하자

- Python3 
  - 장점 : 빠름
  - 단점 : 메모리 사용량이 많음 => 출력 메모리를 줄이자


```python

import sys

# 메모리 사용량 많음
print(n)

# 메모리 사용량을 줄일 수 있음
sys.stdout.write(str(n))
```

# 알고리즘 개념 정리

## Greedy Algorithm

- 정의 
  - 현재 상황에서 지금 당장 좋은 것만 고르는 알고리즘
- 특징
  - 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력 요구
  - 아이디어가 정당한지 검토할 수 있어야함

- Tip
  - '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준이 제시된다면 **정렬 알고리즘**을 활용

## 그래프 탐색

- 정의
  - 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문

- 특징
  - 대표적으로 Depth First Search, Breadth First search, Best First Search 등의 방법이 있음
  - 반드시 **방문여부를 기록**해야한다 (하지 않을 시, 무한루프에 빠짐)
- Tip
  - 단방향 연결과 양방향 연결을 구분하자 (웬만해서 양방향일 확률이 높음)
  - 완전탐색의 경우, 대체적으로 BFS가 DFS보다 빠름
  - 경로의 특징을 저장해둬야하는 경우 : DFS
  - 최단 경로를 구해야하는 경우 : BFS
- 문제 유형
  - 완전 탐색 
    - 영역의 수를 구하는 문제 (DFS,BFS)
    - 최단 경로(BFS)
    - 탐색 과정에서 제약 사항이 있거나 가중치가 있는 경우 (DFS)
  
### Depth First Search (DFS)

- 정의
  - 그래프 전체를 탐색할 때, 다음 분기로 넘어가기 전에 현재 분기를 완벽하게 탐색하고 넘어가는 알고리즘
- 특징
  - Stack 또는 Recursion 사용(LIFO)
  - BFS보다 구현이 간단하다

- 장점
  - 구현이 간단하다.
  - 현재 경로의 노드만 기억하면 되므로, 저장 공간을 덜 차지함
  - 경로의 특징(가중치, 노드 번호 등)을 저장해둬야하는 경우 유용
- 단점
  - 단순 검색에서 BFS보다 속도가 느리다
  - 너무 깊은 단계까지 빠질 가능성이 있다.

- Tip
  - recursion 깊이 조절 :  ```sys.setrecursionlimit(N)```
  - 백트래킹(가지치기)을 잘 활용해서 최대한 깊이를 줄이자
  - 그래프가 이진 트리의 모양이 나오면 시간복잡도가 O(2^N)이 나온다. DP를 이용하자.

- Template
```python
def dfs(graph,visited,V):

  # 필요한 내용 여기서 구현
  
  for v in graph[V]:
    
    if not visited[v]:
    
      visited[V] = True
      dfs(graph,visited,v)
```

>[참고 URL](https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html)

### Breadth First Search (BFS)

- 정의
  - 그래프 전체를 탐색할 때, 인접한 노드를 먼저 탐색하는 방법
- 특징
  - Queue 사용(FIFO)
  - 거리에 따라 단계별로 탐색
  
- 장점
  - 단순 검색에서 DFS보다 속도가 빠르다. (함수를 호출하지 않기 때문에)
  - 최단 거리를 보장해준다. (인접한 노드 먼저 방문하기 때문에)
- 단점
  - DFS보다 구현이 복잡하다.

- Tip
  - Collections 라이브러리의 deque를 사용하자(popleft(), append() : O(1))

- Template
```python
def bfs(graph,visited,V):

  queue = deque([V])
  visited[V] = True
  
  while queue:
    
    v = queue.popleft()
   
    # 필요한 내용 여기서 구현
    
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
```

>[참고 URL](https://gmlwjd9405.github.io/2018/08/15/algorithm-bfs.html)

### Best First Search

- 정의
  - 확장 중인 노드들 중에서 목표 노드까지 남은 거리가 가장 짧은 노드로 확장하는 알고리즘
- 특징
  - Priority queue를 사용
  - Heuristic 탐색 -> 추측을 통해 괜찮은 방향으로 진행하기 때문
  - Greedy Algorithm -> 현재 상황에서 가장 좋은 것을 선택하기 때문
  - 다익스트라 알고리즘과 다르게 늘 최단 거리를 보장하는 것은 아님

- Template
```python

from heapq import heappush, heappop

def bestfs(graph,visited,V):

  queue = []
  heappush(queue,(0,V))
  visited[V] = True
  
  while queue:
    
    dist,now = heappop(queue)
   
    # 필요한 내용 여기서 구현
    
    for i in graph[now]:
      if not visited[i]:
        visited[i] = True
        heappush(queue,(dist+1,i))
```

### Backtracking

- 정의
  - 답이 될만한지 판단하고, 그렇지 않으면 탐색하지 않고 돌아가는 기법

- 특징
  - 완전탐색에서 주로 사용(DFS,BFS)
  - 탐색 횟수를 상당히 줄여준다.
- Tip
  - Stack 또는 queue에 넣기전에 먼저 유망성 검사를 해주면 더 효율적임(이미 방문했는지, 허용 범위를 넘어가지 않는지 등)

>[참고 URL](https://chanhuiseok.github.io/posts/algo-23/)

## 최단 경로 탐색

- 정의
  - 가장 짧은 경로를 찾는 알고리즘

- 특징
  - Vertex(국가, 지역 등), Edge(다리, 도로 등)으로 표현된 그래프가 주어짐 

- 문제유형
  - ① 하나의 정점에서 다른 하나의 정점까지의 최단 거리를 구하는 문제
  - ② 하나의 정점에서 다른 모든 정점까지의 최단 거리를 구하는 문제 (다익스트라 알고리즘)
  - ③ 하나의 목적지까지의 모든 최단 경로
  - ④ 모든 정점에서 다른 모든 정점까지의 최단 거리를 구하는 문제 (플로이드 워셜 알고리즘)

### 다익스트라 알고리즘

- 정의
  - 다익스트라가 제안한 하나의 정점에서 다른 모든 정점까지의 최단 거리를 구하는 알고리즘
- 특징
  - 1차원 그래프뿐만 아니라 2차원 
  - 시작점과의 거리를 기준으로 다음 경로를 설정함(Best First Search와의 차이점) -> 최단 거리를 보장해줌
  - 음의 간선이 없을 때 가능
  - 매 상황에서 가장 비용이 적은 vertex를 선택 (Greedy Algorithm)
  - 네트워크 경로 설계에 많이 적용 -> 라우팅 프로토콜 OSPF(Open Shortest Path First)

- 시간복잡도
  - 선형탐색 : O(V^2) (Vertex 5000개까지 가능)
  - Priority Queue 사용 : O(ElogV) (Edge 10~20만개 / Vertex 1만개 이상 가능)
 
- 동작 과정
  - 출발 노드 설정
  - 최단 거리 테이블 초기화
  - 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택
  - 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해서 최단 거리 테이블 갱신

- Tip
  - 그래프를 통해 최단 경로, 최소 비용, 최소 시간를 구하는 문제라면 다익스트라 알고리즘을 떠올린다.
  - 해당 문제에 다익스트라 알고리즘을 적용할 수 있는지 생각해본다. (예를 들어,하나의 노드에서 다른 노드로의 최단 경로인 경우)
  - O(ElogV)으로 해결 가능한지 시간복잡도를 계산해본다.

- 선형탐색 Template

```python
INF = int(1e9)

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

def get_smallest_node():
  min_value = INF
  index = 0
  
  for i in range(1,N+1):
    if distance[i] < min_value and not visited[i] :
      min_value = distance[i]
      index = i
  
  return index

def dijkstra(start):
  
  distance[start] = 0
  visited[start] = True
  
  for i in graph[start] :
    distance[i[0]] = i[1]
  
  for i in range(N-1):
    
    now = get_smallest_node()
    
    visited[now] = True
    
    for j in graph[now]:
      cost = distance[now] + j[1]
      
      if cost < distance[j[0]]:
        distance[j[0]] = cost
```

- 우선순위 큐 Template

```python
import heapq

INF = int(1e9)

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

def dijkstra(start):
  
  q = []
  
  heapq.heappush(q,(0,start))
  distance[start] = 0
  
  while queue:
    
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
      continue
     
     for i in graph[now]:
      
      cost = i[1] + dist
      
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush((cost,i[0]))
```

### 플로이드 워셜 알고리즘

- 정의
  - 플로이드가 제안한 모든 정점간의 최단 거리를 구하는 알고리즘
- 특징
  - 2차원 리스트 사용
  - 음의 간선이 있을 때도 사용 가능
  - 모든 노드에서 다른 모든 노드까지의 최단 경로 보장
  - 거쳐 가는 노드를 기준으로 알고리즘을 수행 -> a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사
  - 점화식 : Dab = min(Dab, Dak+Dkb) -> Dynamic programming

- 시간복잡도
  - O(V^3) (Vertex 250-300개까지 가능)
 
- 동작 과정
  - 최단 거리 테이블 초기화 (a->a인 경우는 0으로 초기화)
  - k번 노드를 거쳐가는 경우를 고려하여 최단 거리 테이블 갱신 

- Tip
  - 노드의 수가 적고 인접 행렬이 주어지면 플로이드 워셜을 떠올리자
  - 최단 경로뿐만 아니라 경로의 유무를 물어보는 문제에서도 사용 (graph[i][k] == 1 and graph[k][j] == 1이면 경로가 존재)
  - 사람간의 관계를 묻는 문제가 나온다면, 플로이드 워셜을 떠올려보자 (예를 들어, a와 b가 친구인지, 건너서 아는 사이인지, 건너 건너 아는 사이인지 등)

- Template

```python
INF = int(1e9)

graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
  for j in range(1,N+1):
    if i == j :
      graph[i][j] = 0

for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
      
```

### Disjoint set (서로소 집합)

- 정의
  - 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조 (Union Find 자료구조)

- 종류
  - Union(합집합) : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
  - Find(찾기) : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
 
- 특징
  - 노드간의 연결성을 집합의 형태로 손쉽게 확인할 수 있다.

- 시간복잡도
  - O(V)

- Union 동작 과정
  - 여러 Union 연산(Edge)이 주어진다.
  - 해당 Union 연산의 A와 B 노드의 루트 노드 A', B'를 찾는다.
  - A'를 B'의 부모 노드로 설정 (큰 노드를 작은 노드의 부모로 설정하는 것이 관례)
  - 모든 Union 연산에 반복

- Find 동작 과정
  - 부모 테이블에서 해당 노드의 부모를 확인
  - 만약 부모와 해당 노드가 같다면 해당 노드를 리턴(본인이 루트)
  - 만약 부모와 해당 노드가 다르다면, 재귀적으로 부모 노드를 Find 함수로 다시 호출

- Tip
  - 마지막에 부모테이블 최신화를 해주자(하지 않는 경우, 정답이 달라질 수도 있음)
 
- Template
```python

# 단순히 부모 노드를 찾는 경우
def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent,parent[x])
  
  return x
  
# 부모 테이블을 루트 노드로 갱신하는 경우 (시간복잡도가 개선됨)

def find_parent(parent,x):
  
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  
  return parent[x]
  
def union_parent(parent,a,b):
  
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  
  if a<b:
    parent[b] = a
  else:
    parent[a] = b


# 부모 테이블을 자기 자신으로 초기화
for i in range(1,V+1):
  parent[i] = i

# Edge 별로 Union 연산
for i in range(E):
  a,b = map(int,input().split())
  union_parent(parent,a,b)
  
# 부모테이블 루트 노드로 최신화
for i in range(N):
  find_parent(parent,i)
```

- 서로소 집합을 활용한 사이클 판별(무방향 그래프)
```python

def find_parent(parent,x):
  
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  
  return parent[x]
  
def union_parent(parent,a,b):
  
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

for i in range(1,V+1):
  parent[i] = i

cycle = False

# 서로 루트 노드가 같은데 Edge로 연결된다면 사이클이 발생한 것임
for i in range(E):
  a,b = map(int,input().split())
  
  if find_parent(parent,a) == find_parent(parent,b):
    cycle = True
    break
  else:
    union_parent(parent,a,b)
    
```



## Dynamic Programming

- 정의
  - 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법

- 조건
  - ① : Optimal Substructual(최적 부분 구조)
    - 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아서 큰 문제를 해결하는 경우
  - ② : Overlapping Subproblem(중복되는 부분 문제)
    - 동일한 작은 문제를 반복적으로 해결하는 경우

- 종류
  - ① Top down (Memoization)
    - 큰 문제를 해결하기 위해 작은 문제를 재귀적으로 호출 (DFS)
    - 이미 해결한 문제의 값은 메모리에 저장해놓고, 반복 호출시 메모리에서 값을 가져온다(Memoization)
  - ② Bottom up
    - 작은 문제를 해결해나가며, 먼저 계산한 문제의 값을 활용하여 다음 문제들을 해결(반복문)
    - 점화식 도출

- Tip
  - 큰 문제가 작은 문제로 나눠지지만, 중복 연산이 없는 경우 : Divide and conqure
  - 큰 문제가 작은 문제로 나눠지고, 중복 연산이 있는 경우 : Dynamic programming

- 문제 유형 Tip
  - DP 문제인데 "입력 개수가 적거나", "입력 값이 작다면" 2차원 리스트 or 3차원 리스트를 통해 해결할 수 있는지 생각해보자
  - 왼쪽, 중앙, 오른쪽처럼 방향이 주어진 문제는 인접한 DP를 통해 값을 구해보자(예를 들어, 왼쪽인 경우: dp[1]+dp[2] / 중앙인 경우 : dp[0] + dp[2] / 오른쪽인 경우 : dp[0]+dp[1]) 
  - 도형 문제, 주어진 수(ex : 1,2,3)를 활용하는 문제라면 **피보나치 수열**을 떠올려보자 (DP[i] = DP[i-1] + DP[i-2])
  - 선분이 겹쳐진 것을 해결하는 문제, 작은 상자를 큰 상자에 넣는 문제(가장 길게 증가하는 부분) -> **LIS**를 떠올려보자

### 0-1 Knapsack Problem

- 정의
  - 배낭의 최대값이 정해져 있고, 일정 가치와 무게가 존재하는 물건들을 배낭에 넣을 때 가치의 합이 최대가 되도록하는 알고리즘

- 조건
  - ① 물건을 부분적으로 담을 수 없다. (Fraction X)
  - ② 물건들은 모두 한개만 존재한다.

- 아이디어
  - i번째 물건을 배낭에 넣을 수 없는 경우(배낭 무게 초과) : 현재 무게와 가치를 유지한다.
  - i번째 물건을 넣을 수 있는 경우 : "i번째 물건의 무게를 뺀 배낭의 최대 가치 + i번째 물건의 가치"와 "i번째 물건을 넣지 않을 때의 최대 가치" 중 더 큰 것을 선택

- 점화식
  - DP[i][w] = DP[i-1][w] (wi > w)
  - DP[i][w] = max(DP[i-1][w-wi] + arr[i], DP[i-1][w])

- 시간 복잡도
  - O(N^2)

- Tip
  - 한정된 자원(배낭의 무게, 피로도 등)과 가치(돈, 행복 등)가 주어지면 0-1 Knapsack Problem으로 접근하자.
  - DP[한정된 자원 크기][가치의 개수]를 만들자

- Source code(DP)

```python

# W : 배낭 무게 상수
# L : 물건별 무게
# P : 물건별 가치

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1,N+1):
  for w in range(1,W+1):

    if L[i] > w :
      dp[i][l] = dp[i-1][w]
    else:
      dp[i][l] = max(P[i]+dp[i-1][w-L[i]],dp[i-1][w])
    
```

### 주어진 수를 통해서 특정 값을 만드는 경우의 수

- 정의
  - 몇가지 수를 주고 특정 값을 만드는 경우의 수를 구하라는 문제 유형

- 아이디어
  - 주어진 수들을 정렬
  - dp[주어진 수의 개수][만들고자 하는 값]으로 리스트를 생성 (1,2,3이 주어지고 10을 만드는 경우의 수 : dp[3][10])
  - i번째 수(P[i])보다 j가 더 작다면, 해당 수로 j를 만들지 못하기 때문에 i-1번째 개수를 들고온다.
  - i번째 수보다 j가 더 크거나 같다면, 해당 수로 j를 만들 수 있기 때문에, i번째 수를 통해 j-P[i]를 만드는 경우의 수 + 1을 해준다. (해당 수를 넣는 경우가 하나가 추가 됐기 때문에 1을 더해줌)

- 점화식
  - DP[i][j] = DP[i-1][j] (j < P[i])
  - DP[i][j] = DP[i][j-P[i]] + 1 (j >= P[i])

- 시간 복잡도
  - O(N^2)

- Source code(DP)

```python

dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][0] = 1
  
for i in range(1,N+1):
  for j in range(M+1):
  
    if coins[i]<=j:
      dp[i][j] = dp[i][j-P[i]]+dp[i-1][j]
    else:
      dp[i][j] = dp[i-1][j]
    
```


### 연속 부분 최대합(구간합)

- 정의
  - 정수로 이루어진 수열에 대해, 연속된 부분구간 중 그 합이 최대가 되는 구간을 찾는 유형

- 아이디어
  - i-1번째까지의 합이 0보다 작으면 새로 시작하는 것이 더 낫다.
  
- 점화식
  - DP[i] = max(0,DP[i-1])+arr[i] (i>0)
  - DP[i] = arr[i] (i=0)

- 시간 복잡도
  - O(N)

-Source Code (DP)

```python

# arr : 정수로 이뤄진 리스트

dp[0] = arr[0]

for i in range(1,len(arr)):
  dp[i] = max(0,dp[i-1]) + arr[i]
    
```

### LIS (Longest Increasing Subsequence)

- 정의
  - 주어진 수열 내에서 증가하는 가장 긴 부분 수열을 찾아내는 알고리즘

- 아이디어
  - arr[:i] 중 arr[i]보다 작은 값이 있다면, i번째를 포함하는 부분 수열은 해당 부분 수열보다 1만큼 더 길다.
  - 그 중 가장 긴것이 LIS가 된다.

- 점화식
  - DP[i] = max(DP[i], DP[j]+1) (if, arr[i] >arr[j])

- 시간 복잡도
  - O(N^2)
  - Binary search : O(NlogN)

- Source code(DP)

```python

for i in range(N):
  dp[i] = 1
  
  for j in range(i):

    if data[j] <data[i]:
      dp[i] = max(dp[i],dp[j]+1)
    
```


## Sorting

### Counting sort

- 정의
  - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 효율적인 정렬 알고리즘

- 방법
  - 데이터의 크기 범위만큼의 배열 생성
  - 정수의 등장횟수를 배열에 저장(Coungting)
 
- 특징
  - 동일한 값을 가지는 데이터가 여러 번 등장할 때 효과적
  - 시간 복잡도 : O(N+K)
  - 최대값에 따라 시간복잡도, 공간복잡도가 영향을 받음(만약 최대값이 너무 크면, 배열을 크게 만들게 되고 for문도 많이 돌게됨)

- Template
```python

count = [0] * (N+1)

# Counting
for i in range(len(array)):
  count[array[i]] += 1
 
# 배열의 크기(최대값)에 따라 반복 횟수가 증가함
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
    
```
>[참고 URL](https://bowbowbow.tistory.com/8)

### Quick selection

- 정의
  - 리스트를 정렬하지 않고 K번째로 크고 작은 수를 찾는 알고리즘

- 방법
  - Quick sort에서 pivot과 찾으려는 index를 비교(같다면 return / 작다면 left만 수행 / 크다면 right만 수행)
 
- 특징
  - 시간 복잡도 : O(N)

- Template
```python

def quick_selection(arr, start, end, key):
  
  if start >= end:
    return
  
  pivot = start
  left = start + 1
  right = end
  
  while left <= right :
    
    # 왼쪽부터 pivot보다 큰 수 탐색
    while left<=end and arr[pivot]>=arr[left] :
      left+=1
    
    # 오른쪽부터 pivot보다 작은 수 탐색
    while start<right and arr[pivot]<=arr[right] :
      right-=1
    
    # 모두 탐색했다면 pivot과 중심값을 교환
    if left>right:
      arr[pivot], arr[right] = arr[right], arr[pivot]
      
    else:
      arr[left], arr[right] = arr[right], arr[left]
   
  # 만약 찾으려는 index과 pivot이 같다면 return
  if key == right:
    return arr[right]
  
  # 만약 찾으려는 index이 pivot보다 작다면 왼쪽만 탐색
  elif key<right:
    quick_selection(arr,start,right-1,key)
    
  # 만약 찾으려는 index이 pivot보다 크다면 오른쪽만 탐색
  else:
    quick_selection(arr,right+1,end,key)
    
```
>[참고 URL](https://debuglog.tistory.com/70)

### 다중 조건 정렬

- 정의
  - 여러 조건을 만족하는 정렬

```python

# x[1] : 첫번째 조건(오름차순)
# -x[2] : 두번째 조건(내림차순)
# x[3] : 세번째 조건(오름차순)

array.sort(key = lambda x : (x[1],-x[2],x[3])
```

## Search

### Parametric Search

- 정의
  - 최적화 문제를 결정 문제(yes or no)로 바꿔서 해결하는 알고리즘
  - 주어진 범위 내에서 원하는 값 또는 원하는 조건에 가장 일치하는 값을 찾는 알고리즘

- 방법
  - 주어진 범위를 정렬한다.
  - 중간 값이 조건을 만족하는 경우, 만족하는 방향으로 start,end 값을 조정한다.
  - start <= end를 만족하지 않는 경우, 결과값을 리턴한다.
 
- 특징
  - 시간 복잡도 : O(logN)

- Tip
  - 주어진 범위 내(엄청나게 큰 범위)에서 최솟값, 최댓값을 구하는 문제 중 결정 문제로 바꿀 수 있다면 활용
  - 처음에 start, end 범위를 구하는 것이 가장 중요
  - 최솟값을 구하는 경우, 왼쪽(end-1)에서 결과값이 나온다. (주어진 조건을 만족하는 동시에 가장 작은 것을 구하기 때문)
  - 최댓값을 구하는 경우, 오른쪽(start+1)에서 결과값이 나온다. (주어진 조건을 만족하는 동시에 가장 큰 것을 구하기 때문)
 
```python

def parametric(M):
  
  start = 0
  end = 10**9
  result = 0
  
  while start<=end:
    
    mid = (start+end)//2
    target = 0
    
    # 여기서 target 조건 계산
     
    if  target <= M:
      end = mid-1
      result = mid
    else:
      start = mid+1

  return result
```

## 기타

### 특정 범위 데이터 개수 구하기

- Tip
  - 주어진 리스트가 정렬 가능한 개수인지 계산 (O(nlogN))
  - 정렬 가능하다면 사용, 정렬 불가능하다면 다른 방법 사용

```python

import sys
from bisect import bisect_left,bisect_right

def count_by_range(arr,left,right):
  
  right_index = bisect_right(arr,right)
  left_index = bisect_left(arr,left)
  
  return right_index - left_index
```


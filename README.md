# Algorithm-Test-Exercise
> 코딩테스트를 대비한 문제 풀이를 정리하는 Repository입니다.

## 코딩테스트를 위한 파이썬

### 시간 복잡도
- 1초에 1000-2000만번 연산 가능
- N의 범위
  - 500 : O(N**3)
  - 2000 : O(N**2)
  - 100,000 : O(NlogN)
  - 10,000,000 : O(N)
 
### 데이터 수와 breaking posint를 정해주지 않을 때



```python

while True:
    try: n = 
      int(input())
      
      # 여기서 계산하고 출력
      
    except:
      break 

######

import sys

N = list(map(int, stdin.read().split()))

for n in N:
  # 여기서 계산하고 출력
```

### 재귀 깊이 조절

```python

import sys
sys.setrecursionlimit(10**5)
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
  - 반드시 방문여부를 기록해야한다 (하지 않을 시, 무한루프에 빠짐)
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
  
## Depth First Search (DFS)

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
  - 그래프가 이진 트리의 모양이 나오면 시간복잡도가 O(2**N)이 나온다. DP를 이용하자.

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

## Breadth First Search (BFS)

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


## Backtracking

- 정의
  - 답이 될만한지 판단하고, 그렇지 않으면 탐색하지 않고 돌아가는 기법

- 특징
  - 완전탐색에서 주로 사용(DFS,BFS)
  - 탐색 횟수를 상당히 줄여준다.
- Tip
  - Stack 또는 queue에 넣기전에 먼저 유망성 검사를 해주면 더 효율적임(이미 방문했는지, 허용 범위를 넘어가지 않는지 등)

>[참고 URL](https://chanhuiseok.github.io/posts/algo-23/)


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

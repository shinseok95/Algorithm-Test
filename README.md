# Algorithm-Test-Exercise
> 코딩테스트를 대비한 문제 풀이를 정리하는 Repository입니다.

# 개념 정리

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
  
- Tip
  - 단방향 연결과 양방향 연결을 구분하자 (웬만해서 양방향일 확률이 높음)
  - 완전탐색의 경우, 대체적으로 BFS가 DFS보다 빠름
  - 경로의 특징을 저장해둬야하는 경우 : DFS
  - 최단 경로를 구해야하는 경우 : BFS
- 문제 유형
  - 완전 탐색 
    - 영역의 수를 구하는 문제 (DFS,BFS)
    - 최단 경로(BFS)
## Depth First Search (DFS)

- 정의
  - 그래프 전체를 탐색할 때, 다음 분기로 넘어가기 전에 현재 분기를 완벽하게 탐색하고 넘어가는 알고리즘
- 특징
  - Stack 또는 Recursion 사용
  - BFS보다 구현이 간단하다
  - 반드시 방문여부를 기록해야한다 (하지 않을 시, 무한으로 깊어짐)
- 장점
  - 현재 경로의 노드만 기억하면 되므로, 저장 공간을 덜 차지함
  - 구현이 간단하다
- 단점
  - 단순 검색에서 BFS보다 속도가 느리다
  - 너무 깊은 단계까지 빠질 가능성이 있다.

- Tip
  - recursion 깊이 조절 :  ```sys.setrecursionlimit()``` 
  - 경로의 특징을 저장해둬야하는 경우 유용
  - 가지치기, 백트래킹등을 잘 활용해서 최대한 깊이를 줄이자

```python
def dfs(graph,visited,V):

  # 필요한 내용 여기서 구현
  
  for v in graph[V]:
    
    if !visited[v]:
    
      visited[V] = True
      dfs(graph,visited,v)
```

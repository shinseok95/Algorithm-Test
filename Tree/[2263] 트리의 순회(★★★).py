"""
post_order의 마지막이 부모 노드란 것을 알 수 있었고, in_order를 부모의 왼쪽 오른쪽을 나눈 것 까지는 생각해냈다.

그러나 이를 구현하는데 있어서 실패했고, 결국 정답을 봤으나, 메모리 초과때문에 고생하고있다.

아마도   
center_idx = in_order.index(post_order[post_right])

이부분에서 index를 찾는 것에서 시간초과가 나오는 것 같다.



"""

import sys
sys.setrecursionlimit(10**6)

def divied_conquer(in_left,in_right,post_left,post_right):

  if in_left>in_right or post_left>post_right:
    return

  center_idx = position[post_order[post_right]]

  sys.stdout.write(str(post_order[post_right])+' ')

  left_cnt = center_idx-in_left
  right_cnt = in_right - center_idx

  divied_conquer(in_left,in_left+left_cnt-1,post_left,post_left+left_cnt-1)

  divied_conquer(in_right-right_cnt+1,in_right,post_right-right_cnt,post_right-1)

N = int(sys.stdin.readline())

in_order = list(map(int,sys.stdin.readline().split()))
post_order = list(map(int,sys.stdin.readline().split()))

position = [0]*(N+1)

for i in range(N):
  position[in_order[i]] = i

divied_conquer(0,N-1,0,N-1)

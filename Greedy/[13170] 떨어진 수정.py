"""
문제 지문이 아무리 길어도 그 원리만 파악한다면 짧은 코드로 해결 가능하다는 점을 알 수 있었다.

"""

n,k,p,w = map(int,input().split())

ans =0

for n in range(p//w):
  ans+=1

if p%w != 0:
  ans+=1

print(ans)
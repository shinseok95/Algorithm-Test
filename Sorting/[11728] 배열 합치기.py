import sys

N,M = map(int,sys.stdin.readline().split())

A = list(map(int,sys.stdin.readline().split()))

A+=list(map(int,sys.stdin.readline().split()))

print(*sorted(A))

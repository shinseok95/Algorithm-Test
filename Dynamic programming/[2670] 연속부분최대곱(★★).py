N = int(input())
li = [float(input()) for _ in range(N)]

""""
연속된 수의 곱의 최대값을 구하는 것이므로 
만약 자신 이전의 수들의 최대값이 자기 자신보다 작다면 끊어가야한다.
"""
for i in range(1, N):
    li[i] = max(li[i], li[i]*li[i-1])
print("%.3f" % (max(li)))
print(li)
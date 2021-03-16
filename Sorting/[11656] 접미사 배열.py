import sys

S = list(sys.stdin.readline().rstrip())

data = [ ''.join(S[i:]) for i in range(len(S))]

for s in sorted(data):
  sys.stdout.write(s+'\n')
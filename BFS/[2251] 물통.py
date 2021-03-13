from collections import deque

def bfs(visited,A,B,C):
  
  queue = deque([(0,0,C)])
  visited.append((0,0,C))

  while queue:
    
    a,b,c = queue.popleft()

    if a==0:
      global result
      result.append(c)

    if a !=0:
      
      # a->b

      if a<=(B-b):
        
        if visited.count((0,a+b,c))==0:
          visited.append((0,a+b,c))
          queue.append((0,a+b,c))

      else:
        if visited.count(((a-(B-b)),B,c))==0:
          visited.append(((a-(B-b)),B,c))
          queue.append(((a-(B-b)),B,c))

      # a->c

      if a<=(C-c):
        
        if visited.count((0,b,a+c))==0:
          visited.append((0,b,a+c))
          queue.append((0,b,a+c))

      else:
        if visited.count(((a-(C-c)),b,C))==0:
          visited.append(((a-(C-c)),b,C))
          queue.append(((a-(C-c)),b,C))
        
        
    if b !=0:

      #b->a

      if b<=(A-a):
        
        if visited.count((a+b,0,c))==0:
          visited.append((a+b,0,c))
          queue.append((a+b,0,c))

      else:
        if visited.count((A,(b-(A-a)),c))==0:
          visited.append((A,(b-(A-a)),c))
          queue.append((A,(b-(A-a)),c))

      #b->c

      if b<=(C-c):
        
        if visited.count((a,0,b+c))==0:
          visited.append((a,0,b+c))
          queue.append((a,0,b+c))

      else:
        if visited.count((a,(b-(C-c)),C))==0:
          visited.append((a,(b-(C-c)),C))
          queue.append((a,(b-(C-c)),C))
    
    if c !=0:

      #c->a

      if c<=(A-a):
        
        if visited.count((a+c,b,0))==0:
          visited.append((a+c,b,0))
          queue.append((a+c,b,0))

      else:
        if visited.count((A,b,(c-(A-a))))==0:
          visited.append((A,b,(c-(A-a))))
          queue.append((A,b,(c-(A-a))))

      #c->b

      if c<=(B-b):
        
        if visited.count((a,b+c,0))==0:
          visited.append((a,b+c,0))
          queue.append((a,b+c,0))

      else:
        if visited.count((a,B,(c-(B-b))))==0:
          visited.append((a,B,(c-(B-b))))
          queue.append((a,B,(c-(B-b))))
  

A,B,C = map(int,input().split())

visited=[]
result = []

bfs(visited,A,B,C)

result = set(result)
result = list(result)
result = sorted(result)

for i in result:
  print(i,end=' ')
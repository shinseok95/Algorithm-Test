
"""
최대공약수를 이용하는 문제였다.

처음에는 (0,0)과 (w,h)를 통해 기울기를 구하고 for문을 통해 x값을 늘려가며 걸쳐지는 사각형의 개수를 구하였다.

예를 들어, w=8,h=12인 경우 기울기는 12/8이고 
x가 0,1일때, y값을 내림과 올림을 하면 y=0,y=2가 된다.

그렇다면 직선이 지나가는 정사각형은 2-0 = 2개가 된다.

또한, x가 1,2일때, y값을 내림과 올림을 하면 y=1,y=3 , 3-1=2개가 된다.

하지만 이런 방식이 정확한 방식이긴 하나, w,h의 범위가 1억 이하이기 때문에 계속 시간초과가 나왔다.

그래서 결국 정답을 찾아보게 되었고, 최대 공약수를 이용한 방법을 찾을 수 있었다.

우선 최대공약수일 때를 제외하고는 사각형이 w+h개가 된다.

왜냐하면 직선을 그었을 때, 위에서 오는 w개의 사각형+ 옆에서 오는 h개의 사각형이 직선에 겹쳐지기 때문이다.

그러나 만약 최대공약수의 경우, 직선에 겹쳐지는 것이 아니라 점에 겹쳐지게 된다.

즉, 이러한 경우에는 위와 옆에서 오는 2개의 사각형이 생기는 것이 아니라 1개의 사각형만 생기게 되는 것이다.

그렇기에 최종적으로 (w*h)-w-h+gcd(w,h)가 정답이 된다.

"""

def gcd(a,b):
    while b!=0:
        a,b = b,(a%b)
    return a

def solution(w,h):
    
    if w==h:
        return (w*h)-w
    
    elif w==1 or h==1:
        return 0
    
    elif w>h:
        return (w*h)-w-h+gcd(w,h)
    
    else:
        return (w*h)-w-h+gcd(h,w)

"""
from math import floor, ceil
from fractions import Fraction

def solution(w,h):
    
    if w==h:
        return (w*h)-w
    
    elif w==1 or h==1:
        return 0
    
    elif w>h:
        a = Fraction(w,h)
        count = 0

        for x in range(h):
        
            left = floor(a*x)
            right = ceil(a*(x+1))
            
            count += (right-left)
    
        return (w*h)-count
    
    else:
        a = Fraction(h,w)
        count = 0

        for x in range(w):
        
            left = floor(a*x)
            right = ceil(a*(x+1))
            
            count += (right-left)
    
        return (w*h)-count
"""
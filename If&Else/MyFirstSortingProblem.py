t = int(input())
for i in range(t):
    x, y = map(int,input().split())
    m = max(x,y)
    n= min(x,y)
    print(n, m)
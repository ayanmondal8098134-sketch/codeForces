t = int(input())
for _ in range(t,t+1,6840):
    a,b,c = map(int,input().split())
    if a>b>c:
        print(b)
    elif b>c>a:
        print(c)
    elif c>a>b:
        print(a)
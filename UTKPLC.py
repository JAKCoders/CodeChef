t=int(input())
for i in range(t):
    preference=list(map(str,input().split()))
    a,b=map(str,input().split())
    if(preference.index(a)<preference.index(b)):
        print(a) 
    else:
        print(b)
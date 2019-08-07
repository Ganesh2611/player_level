a,b=map(int,input().split())
C=[]
for e in range(a,b+1):
    for d in range(2,e):
        if(e%d==0):
            break
    else:
        C.append(e)
print(len(C))

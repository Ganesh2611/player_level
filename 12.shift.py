a,b=map(int,input().split())

c=[]
l=list(map(int,input().split()))
c=(l[-b:]+l[:-b])
for i in range(0,len(c)):
	print(c[i],end=" ")

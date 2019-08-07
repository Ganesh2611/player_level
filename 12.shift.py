a,d=map(int,input().split())
c=[]
l=list(map(int,input().split()))
c=(l[-d:]+l[:-d])
for i in range(0,len(c)):
	print(c[i],end=" ")

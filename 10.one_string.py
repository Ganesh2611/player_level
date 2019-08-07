s,s1=input().split()
A=0
for i in range(0,len(s)):
    for j in range(0,i+1):
        if s[i]!=s1[j]:
            A+=1
            break
if A==1:
    print("yes")
else:
    print("no")

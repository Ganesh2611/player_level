a=int(input())
b=0
c=0
while(a!=0):
  c=a%10
  b=(b*10)+c
  a=int(a/10)
print (b)

A=input()
print(''.join([A[b:b+2][::-1] for b in range (0,len(A),2)]))

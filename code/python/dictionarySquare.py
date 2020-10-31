#dictionary which stores square of a number upto given limit
n=int(input())
d={}
for i in range(1,n+1):
  d[i]=i*i
print(d,end='')

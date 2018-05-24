import math
l,r=list(map(int,input("Enter the number:").split()))
c=0
for i in range(l,r+1):
  a=math.sqrt(i)
  if(a==int(a)):
    c=c+1
print(c)

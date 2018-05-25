n=int(input("Enter the number:"))
a=list(map(int,input("Enter the number:").split(" ")))[:n]
c=0
if(n==1):
  print(a)
else:
  for i in range(1,len(a)):
    c=c+a[i]+a[i-1]
  print(c)

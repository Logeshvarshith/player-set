n=int(input("Enter the number:"))
d=[]
a=list(map(int,input("Enter a").split(" ")))[:n]
c=0
for i in range(0,len(a)):
  c=c+a[i]
  d.append(c)
print(" ".join(str(x) for x in d))

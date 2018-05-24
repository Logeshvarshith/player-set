l,r=map(int,input("Enter the number:").split(" "))
if(l>r):
  a=l
else:
  a=r
for i in range(a,100000):
  if(i%l==0 and i%a==0):
    print(i)
    break

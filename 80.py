n=int(input("Enter the n:"))
a=[]
for i in range(0,n):
  b=int(input("Enter the number:"))
  a.append(b)
a.sort()
print(a[1]-a[0])

n=int(input("enter the number:"))
a=[]
for i in range(0,n):
  b=int(input("Enter the array:"))
  a.append(b)
s=a[0]
for i in a:
  s=s&i
print(s)

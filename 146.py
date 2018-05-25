a,b=map(int,input("Enter the number:").split(" "))
def fact(n):
  c=1
  for i in range(1,n+1):
    c=c*i
  return c
print(int(fact(a)/fact(b)))

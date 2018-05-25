n=int(input("Enter the number:"))
if(n==2):
  print("yes")
for i in range(2,n):
  if(n%i==0):
    print("yes")
    break
  else:
    print("no")
    break

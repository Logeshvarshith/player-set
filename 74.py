n=input("Enter the n:")
for i in n:
  if(n.count(i)>1):
    print("yes")
    break
else:
  print("no")

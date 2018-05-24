x1,y1=map(int,input("Enter !st line").split(' '))
x2,y2=map(int,input("Enter 2nd line").split(' '))
x3,y3=map(int,input("Enter 3rd line").split(' '))
b=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
if(b==0):
  print("yes")
else:
  print("no")

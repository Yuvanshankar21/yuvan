n=int(input("Enter number:"))
t=n
r=0
if n<=1000:
    while(n>0):
     d=n%10
     r=r*10+d
     n=n//10
    if(t==r):
      print("yes")
    else:
      print("no")
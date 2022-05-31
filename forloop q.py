a=1
n=int(input("enter"))
for i in range (n):
    for j in range (i+1):
      print(a,end=" ")
    print()
    a=a+2
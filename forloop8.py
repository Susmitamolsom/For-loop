n=int(input("enter"))
for i in range (n+1):
    for j in range (n):
        if j==0 or j==4 and i==1 or i==2 or i==0 or j==i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
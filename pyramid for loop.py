n=int(input("enter"))
for raw in range (1,n+1):
    for col in range (1,2*n):
        if raw==n or raw+col==n+1 or col-raw==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
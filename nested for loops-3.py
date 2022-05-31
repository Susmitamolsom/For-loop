n=int(input("enter rows"))
for i in range(n):
    for b in range(i):
        print(" ",end=" ")
    for j in range(2*(n-i)-1):
        print("*",end=" ")
    print()        
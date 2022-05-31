n=int(input("enter"))
for i in range (n):
    for j in range (n-i-1):
        print(" ",end=" ")
    for b in range (2*i+1):
        print("*",end=" ")
    print()
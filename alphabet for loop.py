n=int(input("enter"))
for i in range (n):
    for j in range (i,-1,-1):
        print(chr(65+j),end=" ")
    print()
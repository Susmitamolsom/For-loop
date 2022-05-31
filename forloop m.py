a=1
n=int(input("enter"))
for i in range (1,n+1,2):
    for j in range (1,i+1):
        print(a,end=" ")
        a=a+1
    print()
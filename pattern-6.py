n=int(input("Enter max no of rows: "))

i=1
while i<=n:
    print(" " * (n-i),end="")
    j=1
    while j<=2*i-1:
        print(j,end="")
        j+=1
    print()
    i+=1
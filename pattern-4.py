n=int(input("Enter max no of rows: "))

i=n
while i>=1:
    j=n
    while j>=n-i+1:
        print(j,end="")
        j-=1
    print()
    i-=1
    
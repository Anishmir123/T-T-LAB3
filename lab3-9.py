def print_pattern(n):
    for i in range(n):
        if i%2==0:
            for j in range(1,i+2):
                print(j,end=" ")
        else:
            for j in range(i,-1,-1):
                print(j+1, end=" ")
        print()
n = int(input("Enter number:"))
print_pattern(n)
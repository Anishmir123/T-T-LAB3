def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            if (i+j)%2==0:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
n = int(input("Enter number:"))
print_pattern(n)

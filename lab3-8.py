def print_pattern(n):
    for i in range(n):
        for j in range(i,-1,-1):
            print(chr(65+j), end=" ")
        print()
n = int(input("Enter number:"))
print_pattern(n)
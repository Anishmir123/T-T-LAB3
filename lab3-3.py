num =int(input("Enter the number: "))

rev=0
while num>0:
    rev=(rev*10)+num%10
    num=num//10
print("Reverse number are",rev)
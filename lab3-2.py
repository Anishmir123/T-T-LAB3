#WAP to calculate the sum of digit of a given number
num = int(input("Enter the number: "))

sum=0
while num>0:
    sum=sum+num%10
    num=num//10
print("sum of digit: ",sum)

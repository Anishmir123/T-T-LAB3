#WAP to calculate the factorial of a given number
num = int(input("Enter the number: "))
fact=1
if(num<0):
    print("fact is not exist")
if(num==0):
    print("fact is 0",1)
if(num>0):
    for i in range(1,num+1):
        fact=fact*i
print("the factorial number is :",fact)

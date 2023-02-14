def findHCF():
    if x>y:
        smaller = y
    else:
        smaller = x
        for i in range(1,smaller+1):
              if((x%i==0) and (y%i==0)):
                hcf = i
    return hcf
x=30
y=20
print("Find the two hcf number",findHCF())


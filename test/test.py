'''
print("this is for python program")
x = int(input("enter the number"))
y = int(input("enter the number"))
print("addiition is",x+y)
if x>y:
    print(x, " is maximum")
    print(str(x)+" is maximum")
    if x==y:
        print("yes")
    else:
        print("no")
else:
    print(y,"is maximum")
    print(str(y)+" is maximum")       
      

x = int(input("Put Value For X : "))
y = int(input("Put Value For Y : "))
z = int(input("Put Value For Z : "))

if x>y>z:
    print("X is Gretar than Y and Z")
elif y>x>z:
    print("Y is Greter than X and Z")
else:
    print("Z is Greter than X and Y")

'''

p = float(input("Enter Principle value : "))
i = float(input("Interest rate : "))
n = int(input("Duratiob in years "))



if p<10000:

    print("total interst is = ",(p*i*n)-p)
else:
    

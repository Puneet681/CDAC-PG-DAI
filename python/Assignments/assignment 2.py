#Q1)
'''
a=0
for i in range(10):
    a = a + int(input("enter an interger"))
print("avrage of entered integers is = ",a/10)
'''

#Q2 a)
'''
for i in range(1,5):
    print("*"*i)
'''
#Q2 b)
n=7
for i in range(1,n+1):
    if i%2!=0:
        x= (n-i)//2
        print(" "*x,"*"*i)
for i in range(n-1,0,-1):
    if i%2!=0:
         x= (n-i)//2
         print(" "*x,"*"*i)


#Q3)
'''
x = int(input("enter 1st number"))
y = int(input("enter 2st number"))

def hcf(x,y):
    for i in range(x,0,-1):
        if x%i==0 and y%i==0:
            print(i,f" is the HCF of {x} , {y}")
            break
if x>=y:
    hcf(x,y)
else:
    hcf(y,x)
'''

#Q4)
'''
a=[]
s = 0
m = 1
while True:
    x = input("enter a number
              :- ")
    if x!="q":
        try:
            a.append(int(x))
            print("press q to get results")
        except:
            print("please enter integers only or press q to get the results")
    elif x=="q":
        for i in range(len(a)):
            s = (s+a[i])
            m = m*a[i]
        break
    
print(f"the avrage of all the entered numbers is {s/len(a)}\nthe product of all the enterd number is {m}")
'''

#Q5)
'''
x = int(input("enter a number to get count of digits and their sum :- "))
n = []
b = 0
while True:
    if x==0:
        break
    a = (x%10)
    b = b+a
    n.append(a)
    x=x//10
    
    print(n)
print("number of digits in enterd number is       = ",len(n))
print("addition of all digits in enterd number is = ",b)

    
'''

#Q6)
'''
x = int(input("enter an interger to get cubes of all number OR press 5 to get cubes from 1 to 4"))

if x!=5:
    for i in range(x):
        print(f"{i}^3 = {i**3}")
else:
    for i in range(5):
        print(f"{i}^3 = {i**3}")
'''

#Q7)
'''
s = 0
a = []
b = []
for i in range(20):
    x = int(input(f"enter {i+1}th number"))
    a.append(x)
    if x%2==0:
        b.append(x)
        s = s+x
print(f"all the even number in \n{a} \nare {b} \nand their sum is {s}")
'''

#Q8)
'''
x = int(input("enter the number of iterations :- "))
l = []
s =0
for i in range(1,x+1):
    b=("9"*i)
    b = int(b)
    s = s+b
    l.append(b)
print(l)
print(s)
'''

#Q9)

'''
x = int(input("enter the vale of X :- "))
r = int(input("enter the number of iterations :- "))
fac = 1
a=1 + x

for i in range(2,r):
    fac = fac*i
    print(fac)
    a = a + ((x**i)/(fac))
    
print(a)
'''

#Q10)

'''
x = int(input("enter the vale of X :- "))
r = int(input("enter the number of iterations :- "))
a=0
l = []
count = 0

for i in range(1,r*2,2):
    b = ((x**i))
    if count%2 !=0:
        l.append(-b)
    else:
        l.append(b)
    count = count+1
for i in range(len(l)):
    a = a+l[i]
print(l)
print(a)
'''

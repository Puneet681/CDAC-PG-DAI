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
'''
for i in range(1,6):
    if i%2!=0:
        x= (5-i)//2
        print(" "*x,"*"*i)
for i in range(3,0,-1):
    if i%2!=0:
         x= (5-i)//2
         print(" "*x,"*"*i)
'''

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
q = ' '
s = 0

while q != 'q':
    a = int(input("Enter The Number : "))
    q = input("Press q if you want to exit")
    s = s + a

print("Sum is : ",s)
'''
a=[]
s = 0
m = 0
while True:
    x = input("enter a number \npressq to get avrage and product of all enterd numbers")
    try:
        if x=="q":
            for i in range:
                s = s+a[i]
                m = m*a[i]
        else:
            a.append(int(x))
            print(a)
    except:
        print("wrong dta type is enters")
print(s , m)
'''

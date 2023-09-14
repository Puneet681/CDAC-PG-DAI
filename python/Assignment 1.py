# Q1)
'''
x = int(input("enter the number classes held"))
y = int(input("enter the number classes attended"))

print(f"the student have attended {(y/x)*100} % class")
if (y/x)>=0.75:
    print("student is elidigble to sit in exam")
else:
    print("student is not elidigble to sit in exam")

'''

#Q2)

'''
a = int(input("enter the ammount"))

notes = [2000,500,100,50,10,5,2,1]
count = [0,0,0,0,0,0,0,0]

while a!=0:
    for i in range(len(notes)):
        if a>=notes[i]:
            a = a - notes[i]
            count[i] = count[i]+1
            break
for i in range(len(notes)):
    if count[i]!=0:
        print(f"{notes[i]} = {count[i]}")

'''

# Q3)
'''
x = int(input("enter the number classes held"))
y = int(input("enter the number classes attended"))
z = input("do student has medical cause (Y/N)")
print(f"the student have attended {(x/y)*100} % class")
if (x/y)>=0.75:
    print("student is elidigble to sit in exam")
else:
    if z=="Y":
        print("student is elidigble to sit in exam because of medical cause")
    else:
        print("student is not elidigble to sit in exam")
'''

#Q4)
'''
x = float(input("enter marks of student"))

if x<=25:
    print("the Grade of Student is F ")
elif 25<x<=45:
    print("the Grade of Student is E ")
elif 45<x<=50:
    print("the Grade of Student is D ")
elif 50<x<=60:
    print("the Grade of Student is C ")
elif 60<x<=80:
    print("the Grade of Student is B ")
else:
    print("the Grade of Student is A ")
'''

#Q6)
'''
x = float(input("enter number to check divisibility"))

if x%5==0 and x%11==0:
    print("entered number is divisible by both 5 & 11")
elif x%5==0:
    print("entered number is divisible by only 5")
elif x%11==0:
    print("entered number is divisible by only 11")
else:
    print("entered number is nither divisible by 5 nor by 11 ")
'''

#Q7)
'''
x = int(input("enter units of electricity consumed"))
bill = 0
x = x-100
if x>100:
    bill = 500
    x = x-100
    bill = bill + (x*10)
    print(f"total bill is {bill}")
else:
    bill = bill + (x*5)
    print(f"total bill is {bill}")
'''

#Q8

'''
x = int(input("enter number to check wether the unit digit is divisible by 3 :- "))

if (x%10)%3==0:
    print(f"unit digit {x%10} is divisible by 3")
else:
    print(f"unit digit {x%10} is not divisible by 3")

'''

#Q9
'''
x = int(input("enter the year to check if its leap year or not"))

if x%4==0 or x%400==0:
    print(f"{x} year is leap year")
else:
    print(f"{x} year is NOT leap year")
'''

#Q10)
'''
x = int(input("enter the Ex-showroom price of bike"))

if x>100000:
    tax = (x/100)*15
    ins = (x/100)*20 
    print(f"road tax  = {tax}")
    print(f"insurance = {ins}")
    print(f"total price to be paid = {x + tax + ins}")
elif 100000>=x>50000:
    tax = (x/100)*10
    ins = (x/100)*8 
    print(f"road tax  = {tax}")
    print(f"insurance = {ins}")
    print(f"total price to be paid = {x + tax + ins}")
else:
    tax = (x/100)*5
    ins = (x/100)*5 
    print(f"road tax  = {tax}")
    print(f"insurance = {ins}")
    print(f"total price to be paid = {x + tax + ins}")
'''
dfuihuirghg

    





























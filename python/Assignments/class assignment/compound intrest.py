p = float(input("enter princple "))
r = float(input("enter rate of intrest "))
n = 1
t = float(input("enter duration in years "))
if p>=10000:
    print("princple is greather than 10000")
    d = n*t
    ammount = ((p*(1+((r/100)/n))**(d)))
    ci = ammount - p

    print("Compound intrest is ", ci)
else:
    print("princple is less than 1000")
    si = (p*r*t)/100
    print("simple intrest is ", si)

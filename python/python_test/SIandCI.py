
p = int(input("Enter Principle : "))
r = float(input("Enter Rate : "))
t =  int(input("Enter Time : "))

SI = (p*r*t)/100
print("Total Interest : ",abs(SI-p))
print("simple Interest is : ",round(SI))

CI = (p*(1+r/100)**t) - p
print("Compound Interest is : ",round(CI,2))                                     


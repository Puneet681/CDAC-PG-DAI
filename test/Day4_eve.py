
#-=-=-=--=-=-=-=-=-=-=-=- packing and unpacking of tuples -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

num = 1,2,'sdf','ggbb'
print(num)

def f1(a,b):
    a = a+10
    b = b+10
    c = a+b
    return a,b,c

data=f1(23,24) # unpacking of tuple
print(data)
x,y,z=f1(23,24)
print(x)

a = 12, #this is tuple not int
print("%d is the number"%(34,))
print(type(a))

def addition(a=2,b=5,c=12,*t): # [ *tuple_name ] add tuple at end to store more vaulues than parameters 
    s = a + b + c
    print(t)
    for n in t:
        s = s + n
    return s

print(addition(1,2,3,4,5,6,7,8,9))

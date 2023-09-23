
# --------compulsory parameters---------
def f1(x,y):
    x = x+10
    y = y+10
    return x+y

# f1(10) -- will cause error - 2 parameters required
# f1() -- error
print(f1(40,50))


# ----------default parameters------------------
def f2(a,b=3,c=3):
    a=b+c
    b=a+c
    return a+b+c

# f2() -- error

print(f2(20,54,20)) # all arguments method
print(f2(20,b=10,c=23)) # using keyword arguments


#----------acessing global variable-------------------------

def f3():
    global cnt  #--------------line required to modify global variable inside function
    print("cnt",cnt)
    cnt = cnt+20
    
cnt = 10
f3()
print(cnt)


#--------scopes in python and acessing the variables of diffrent scopes------------------------------------------------

def f4():
    x = 34
    y = 45
    print("y = ",y)
    print(x)
    def f2():
        global x # ----------using global and nonlocal in same fuction for same variable name will result in ERROR
        nonlocal y #-----------to access the variable declared in parrent function

#=-=-=-=-=-=-=-=-=-every function have only 2 scopes GLOBAL , LOCAL=-==---===-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-
#==-=-=-=-=-=-nested funtions have 3 scopes GLOBAL , LOCAL and NONLOCAL =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        print("y = ",y)
        y=66
        print("y = ",y)
        x=45
        print(x)
    print(x)
    f2()   # ----------------- this fuction can not be called outside f4()(parent fuction)
    print("y = ",y)
    print(x)
    

x = 10
print(x)
f4()
print(x)


#-----------Buildin functions
#-----------number functions
#-----------string functions


#-----------BITWISE OPRATOR----------------

x = 9
print(x,bin(x))
y = 11
print(y,bin(y))

newnum = x<<4
newx=newnum|y
print(newx,bin(newx))

y1 = newx&(int(0b1111))
x1 = newx>>4

print(x1,bin(x1))
print(y,bin(y1))



date = 31
mth = 12
year = 2023

print(date,bin(date))
print(mth,bin(mth))
print(year,bin(year))

newnum = year<<9

print(newnum,bin(newnum))
newmth = newnum|(mth<<5)
print(newmth,bin(newmth))

newdate = newmth|date

print(newdate,bin(newdate))



#------Slicing of String

a = 'this is string'

print(a[::]) #all
print(a[::2]) #even steps
print(a[1::2]) #odd steps
print(a[::-1]) #reverse
print(a[::-2]) #reverse steps
print(a[11:-11:-1])

a = 2023
b = 12
print(a,bin(a))
print(b,bin(b))

new_a = a << 11
print(new_a,bin(new_a))
new_ab = new_a | b
print(new_ab,bin(new_ab))
old_b = new_ab & (int(0b1111))
print(old_b,bin(old_b))
old_a = new_ab >> 11
print(old_a,bin(old_a))



#wriet a program to find all the occurences of cat same for reverse

a = "this is a cat,cat is cute, where is you r cat? mine is here"
pos = 0

for i in range(len(a)):
    pos = a.find("cat",pos+1)
    if pos != -1:
        print(pos)
    else:
        break

pos = 0
print("*"*50)
for i in range(len(a)):
    pos = a.rfind("cat",0,pos-1)
    if pos==-1:
        break
    print(pos)

pos = 0
print("*"*50)
try:
    for i in range(len(a)):
        pos = a.index("cat",pos+1)
        print(pos)
except:
    pass

pos = 0
print("*"*50)
try:
    for i in range(len(a)):
        pos = a.rindex("cat",0,pos-1)
        print(pos)
except:
    pass


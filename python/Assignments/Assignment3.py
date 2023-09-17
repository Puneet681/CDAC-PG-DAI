# Q) day 3 in class assigment
'''
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
'''

# =-=-=-=-=-=-=-=-=-=-=-=-Assignment 3 =-=-=-=-=-=-=-=-=-=-=-

#Q1)

'''
str1 = "Rakeshzippetabb"
str2 = "jazzbonAyxx"
s = input("enter a string with morethan 7 and odd number of char. ")

r = len(s)


if len(s)>=7 and r%2 !=0:
    indexLHS = int((len(s)-3)/2)
    indexRHS = int(indexLHS+3)
i = 1
print(s[indexLHS:indexRHS])
'''

#Q2)
'''
s1 = 'atul'
s2 = 'kelly'
i = (len(s1))//2
print(s1[0:i]+s2+s1[i:])
    
'''

#Q3)
'''
s1 = "america"
s2 = 'japan'

def mix(s1,s2):
    m1 = len(s1)//2
    m2 = len(s2)//2
    l1 = len(s1)-1
    l2 = len(s2)-1
    print(f"{s1[0]+s2[0]}"+f"{s1[m1]+s2[m2]}"+f"{s1[l1]+s2[l2]}")

mix(s1,s2)
'''

#Q4)

'''
str = "PyTHONStudy"
l =[]
u=[]

for i in str:
    if i.islower():
        l.append(i)
    else:
        u.append(i)
lr = "".join(l)
ur = "".join(u)

print(lr+ur)
        
'''

#Q5)

'''
s = "abcd"
s2 = "xyz"
r = 0
if len(s) >= len(s2):
    r = len(s)
    temp = s
    s2 = s2[::-1]
else:
    r = len(s2)
    temp = s2
    s = s[::-1]
print(r)

for i in range(r):
    try:
        print(f"{s[i]}{s2[i]}",end='')
    except:
        print(f"{temp[i]}",end='')

'''

#Q6)


x = "Welcome to USA. usa awesome, isn't it?"
a = x.upper()
b="USA"
pos = a.rfind(b)
while pos != -1:
    print(pos)
    pos = a.rfind(b,0,pos)
print("*"*80)
print("number of occunces :- ",a.count(b))
    
    

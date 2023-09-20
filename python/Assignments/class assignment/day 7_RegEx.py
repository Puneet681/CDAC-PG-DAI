# -=-=-=-=-=-=-=-=-=-=- DAY 7 -=-=-=-=-=--==-=-=-=--=-=-=-=-=-=-=-=-=-

#-------------------- Regular Expression (RegEX) --------------------- 

import re

s = 'something is there somewhere'
# find one occurence from anywere in string
print("this is m")
m = re.search("s.*e",s,re.I|re.M)
print(m)
if m != None:
    print(m.group())
    print(m.span())
else:
    print("not found")

print("--------------------------")

m1 = re.search("s.*?e",s,re.I|re.M)
print(m1)
if m1 != None:
    print(m1.group())
    print(m1.span())
else:
    print("not found")
print("--------------------------")    
    
m2 = re.search("t.*?e",s,re.I|re.M)
print(m2)
if m2 != None:
    print(m2.group())
    print(m2.span())
else:
    print("not found")
    
print("--------------------------")

m2 = re.match("s.*?e",s,re.I|re.M)
print(m2)
if m2 != None:
    print(m2.group())
    print(m2.span())
else:
    print("not found")
    
print("--------------------------")
# find one occurence from start of string 
m2 = re.match("t.*?e",s,re.I|re.M)
print(m2)
if m2 != None:
    print(m2.group())
    print(m2.span())
else:
    print("not found")
    
print("--------------------------")

s = "something is there somewhere"
# find all occurences anywere in string 
m2 = re.finditer('s.*?e',s,re.I|re.M)
print(m2)
if m2 != None:
    for m in m2:
        print(m.group())
        print(m.span())
else:
    print("not found")
    
    
print("--------------------------")

s = "something is there somewhere"
# find all occurences and stores in list 
m2 = re.findall('s.*?e',s,re.I|re.M)
if m2 != None:
    print(m2)
else:
    print("not found")
    
    
print("--------------------------")

s = "something is there somewhere"
# substitudte val in string with new string (here with "any") depend on count
s_new = re.sub("s.*?e","any",s,flags = re.I|re.M , count = 1)  # count = 0 mean replaces all
print(s_new)

print("--------------------------")

s = "something is there somewhere"

myreg = re.compile(("s.*?e"),flags=re.I|re.M)

m2 = myreg.search(s)
if m2 != None:
    print(m2.group())
    print(m2.span())
else:
    print("not found")
    
    
s2 = myreg.sub(s , "any")
print(s2)

print("--------------------------")

mob = (input("enter mob. number"))

m = re.search("[987]\w{9}$", mob)
if m != None:
    print(" mobile no. is valid")
else:
    print("not found")


print("--------------------------")

mob = (input("enter mob. number"))

m = re.search("^\+91-[987]\d{9}$", mob)
if m != None:
    print(" mobile no. is valid")
else:
    print("not found")
    
print("--------------------------")

s = "this is word"

m = re.match("^\w+\s\w+\s\w+$",s)
if m !=None:
    print("found")
else :
    print("found")


print("--------------------------")

s = "this is word"

m = re.match("^(\w+)\s(\w+)\s\w+$",s)
#-------------- (1) -- (2) --- # we can get span and group of subelements by using -> ()
if m !=None:
    print(m.group(),m.span())
    print(m.group(1),m.span(1))
    print(m.group(2),m.span(2))
    print("found")
else :
    print("not found")
    
    
    
print("--------------------------")

ac = "XXXX1234XXXX"

m = re.match("^X{4}(\d{4})X{4}$",ac)
if m !=None:
    print(m.group(1),m.span(1))
    print("found")
else :
    print("not found")
    
print("--------------------------")

s = 'or'

m = re.match("\bor\b",s)
if m !=None:
    print("found")
else :
    print("notfound")
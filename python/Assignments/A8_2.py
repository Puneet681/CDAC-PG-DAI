
import re
path = 'productdata.txt'
copy_path = 'myproduct.txt'
def Q1():
    '''Write a python program to accept mobile number and validate it. it should contain exactly
10 digits.'''
    mob = input("enter mob. number")

    m = re.search("^[987]\d{9}$", mob)
    if m != None:
        print(" mobile no. is valid")
    else:
        print("not found")

def Q2a():
    cf = open(copy_path,'w')
    with open(path,'r') as f:
        for lines in f:
            m = re.search("^12.*0$",lines,re.I|re.M)
            if m != None:
                cf.write(m.group()+"\n")
    cf.close()
def Q2b():
    dir1 ={}
    dir2 = {}
    total = 0
    
    with open(path,'r') as f1:
        for lines in f1:
            
            lines = lines.rstrip('\n')
            lst = lines.split(":")
            if dir1.get(lst[3]) == None:
                s = 0
                dir1[lst[3]] = [lst[4]]
                s = s + int(lst[4])
                dir2[lst[3]] = s
            else:
                dir1[lst[3]].extend([lst[4]])
                s = s + int(lst[4])
                dir2[lst[3]] = s
            total = total + int(lst[4])
    print(dir1)
    print(dir2)
    print(total)

def Q2c():
"""Write a python program to accept category from user, display all products of the given category
Example if category given is chips then use regular expression :chips:
if category given is chips then use regular expression :snack:
generate patter :<givencategory name>: and use it for finding lines of the given category"""
       """
dir1 = {}

dir1 = dir1.fromkeys(list(map(str,input().split())))

print(dir1)
"""

import re 
x = input("Enter Category : ").lower()
with open(path,'r') as p1:
    for lines in p1:
        lines = lines.lower()
        m = re.search(x,lines,re.I|re.M)
        if m != None:
            print(lines)


            
        
        

Q2c()
            
            
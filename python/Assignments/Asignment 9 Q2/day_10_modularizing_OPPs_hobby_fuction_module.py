from Day_10_modularizing_OOps_Hobby import *

l = []
def disp_all():
    for i in l:
        print(i)
        

def add_stud():
    sid = input("enter id")
    name = input("enetr frist name")
    lname = input("enter last name")
    hobbies = []
    while True:
        x = input("add a hobby or press q if done")
        if x == 'q':
            break
        hobbies.append(x)
    mob_no = input("enetr mob_no")
    email = input("enter email")
    bdate = input("enetr D_O_B")
    address = input("enetr address")
    ob = Student(sid,name,lname,hobbies,mob_no,email,bdate,address)
    l.append(ob)
    return ob
    
    
  
def search_by_id():
    sid = input("enter id")
    for i in l:
        sid_c = str(i.get_sid())
        if sid_c == sid:
            return i
        else:
            return None
    
def search_by_name(name):
    
    for i in l:
        n = i.get_name()
        if n == name:
            return i
        else:
            return None

def Hobbies(hobb):
    lst_hobb = []
    for i in l:
        lst = i.get_hobbies()
        for j in lst:
            if j == hobb:
                lst_hobb.append(i)
    if len(lst_hobb) != 0:
        return l
    else:
        return None
            


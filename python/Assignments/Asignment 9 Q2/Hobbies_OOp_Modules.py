from Day_10_modularizing_OOps_Hobby import *

d = {}
def disp_all():
    for k,v in d.items():
        print("id--->",k)
        print("name--->",d[k][0])
        print("lastname--->",d[k][1])
        print("hobbies--->",d[k][2])
        print("mobno--->",d[k][3])
        print("email--->",d[k][4])
        print("bdate--->",d[k][5])
        print("address--->",d[k][6])

def add_stud():
    
    x = int(input("enetr number of students"))
    for i in range(x):
        s = (input("""Enter Value : - 
                   ID ,
                   First_Name, 
                   Last_Name , 
                   Mobile no , 
                   Email , 
                   Date of birth , 
                   Address
                   Enter value : """ )).split(',')
        lst = input("Enter Your hobbies : ").split(',')
        i = Student(s[0],s[1],s[2],lst,s[3],s[4],s[5],s[6])
        k = i.get_sid()
        d[k] = [i.get_name(),i.get_lname(),i.get_hobbies(),i.get_mob_no(),i.get_email(),i.get_bdate(),i.get_address()]
    return d
  
def search_by_id():
    sid = input("Enter id of a Students : ")
    k = d.get(sid)
    if k!=None:
        return (sid,k)
    
def search_by_name():
    name = input("Enter Student Name : ")
    for k,v in d.items():
        if v[0]==name:
            return (k,d[k])

def Hobbies():
    hobb = input("Enter hobby : ")
    for k,v in d.items():
        if hobb in v:
            print(k,v)
            


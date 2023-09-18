import sys
courselst={("DBDA",100),("DAI",40)}
def addnewcourse():
    cname=input("enetr course name")
    capacity=int(input("enetr capacity"))
    courselst.add((cname,capacity))
    return True

def deletecourse():
    val = input("enter course name to be deleted")
    ch = input(f"are you sure you want to del {val} (y\n)")
    if ch == 'y':
        lst_i = list(filter(lambda x:x[0]==val,courselst))
        courselst.remove(lst_i[0])
        print(f" {val} is found been deleted")
        displayall(courselst)
    else:
        print(f"selected n \n {val} is found not deleted")

def coursecapacity():
    val = input("enter course name to be updated")
    cap = input("enter new capacity")
    ch = input(f"are you sure you want to update {val} (y\n)")
    if ch == 'y':
        lst_i = list(filter(lambda x:x[0]==val,courselst))
        courselst.add((val,cap))
        courselst.remove(lst_i[0])
        print(f" {val} is found been modified")
        displayall(courselst)
    else:
        print(f"selected n \n {val} is found not modified")
        displayall(courselst)
    
def displayall(lst=courselst):
    for cname,capa in lst:
        print(f"{cname}--->{capa}")
        
def searchcourses(searchc):
    lst=[]
    for cname,capa in courselst:
        if capa>searchc:
            lst.append((cname,capa))
    return lst
def searchbycname(old):
    for pos,c in enumerate(courselst): #[(0,("DBDA",100)),(1,("DAI",40)))
        if c[0]==old:
            return pos,c
    else:
        return -1,None
        
        
def modifybycourseName():
    val = input("enter course name to be updated")
    n_name = input("enter new name")
    ch = input(f"are you sure you want to update {val} (y\n)")
    if ch == 'y':
        lst_i = list(filter(lambda x:x[0]==val,courselst))
        
        courselst.add((n_name,(lst_i[0])[1]))
        courselst.remove(lst_i[0])
        print(f" {val} is found been modified")
        displayall(courselst)
    else:
        print(f"selected n \n {val} is found not modified")
        displayall(courselst)

choice=0
while True:
    choice = int(input("""
    1. add new course
    2. delete the course
    3. modify course capacity
    4. modify course name
    5. display all
    6. display only courses with capacity > given capacity
    7. exit
    choice:"""))
    if choice==1:
        status=addnewcourse()
        if status:
            print("new course added successfully")
    elif choice==2:
        status=deletecourse()
    elif choice==3:
        status=coursecapacity()
    elif choice==4:
        status=modifybycourseName()
    elif choice==5:
        displayall()
    elif choice==6:
        searchc=int(input("enetr capacity to search courses"))
        lstc=searchcourses(searchc)
        displayall(lstc)
    elif choice==7:
        print("Thank you for visiting....")
        break
    

        



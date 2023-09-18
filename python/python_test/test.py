
import sys
courselst=[("DBDA",100),("DAI",40)]
def addnewcourse():
    cname=input("enetr course name")
    capacity=int(input("enetr capacity"))
    courselst.append((cname,capacity))
    return True

def deletecourse():
    val = input("enter course name to be deleted")
    lst_i = list(filter(lambda x:x[1]==val))
    courselst.remove(lst_i[0])
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
        
        
def modifybycourseName(old,new):
    pos,cdetails=searchbycname(old)
    if pos!=-1:
        ans=input(f"do you want to modify {old} with {new}")
        if ans=="y":
            courselst[pos]=(new,cdetails[1])
            return 1
        else:
            return 2
    else:
        return 3
choice=0
while choice!=7:
    choice =input("""
    1. add new course
    2. delete the course
    3. modify course duration
    4. modify course name
    5. display all
    6. display only courses with capacity > given capacity
    7. exit
    choice:""")

    if choice==1:
        status=addnewcourse()
        if status:
            print("new course added successfully")
    elif choice==2:
        status=deletecourse()
        pass
    elif choice==3:
        pass
    elif choice==4:
        oldcourse=input("enetr old course name")
        newcourse=input("enetr new course name")
        status=modifybycourseName(oldcourse,newcourse)
        if status==1:
            print("found and modification done")
        elif status==2:
            print("found and not modified")
        else:
            print("not found")
    elif choice==5:
        displayall()
    elif choice==6:
        searchc=int(input("enetr capacity to search courses"))
        lstc=searchcourses(searchc)
        displayall(lstc)
    elif choice==7:
        print("Thank you for visiting....")
        #sys.exit(0)








              
    

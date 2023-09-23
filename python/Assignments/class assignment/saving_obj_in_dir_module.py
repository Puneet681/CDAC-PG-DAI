import OOPs_ankush_day_9 as c

empdetails = {}

def displayall():
    for v in empdetails.values():
        print(v,end='')

def addnewemployee(ch):
    enm = input("Enter Name ")
    mob = input("Enter Mobile ")
    dt = input("Enter Department ")
    ds = input("Enter Designamtion ")
    
    if ch == 1:
        s = float(input("Enter Salary : "))
        ob = c.salariedEmp(enm,mob,dt,ds,s)
    else:
        hr = int(input("enter hours"))
        ob = c.ContractEmp(enm,mob,dt,ds,hr)
    empdetails[ob.get_pid()] = ob
        
def deleteemp(eid):
    v = empdetails.get(eid,-1)
    if v != -1:
        ch = input("do you want to delete {eid}\n(y/s)")
        if ch == "y":
            empdetails.pop(eid)
            return 1
        else:
            return 2
    else:
        return 3
    
def modifydetails(eid,s=0,ch=1):
    v = empdetails.get(eid,-1)
    if v != -1:
        if isinstance(v,c.salariedEmp):
            v.set_sal(s)
        else:
            v.set_hrs(s)
            v.set_charges(ch)
            
def findByType(ch):
    lst = []
    if ch == 1:
        for v in empdetails.values():
            if isinstance(v,c.salariedEmp):
                lst.append(v)
    else:
        if v in empdetails.values():
            if isinstance(v,c.ContractEmp):
                lst.append(v)
        
    if lst:
        return lst
    else:
        return None
    
def findBysalary(sal):
    lst = []

    for v in empdetails.values():
        if isinstance(v,c.salariedEmp):
            if v.get_sal()>sal:
                lst.append(v)
        else:
            if v.get_charges()>sal:
                lst.append(v)
        
    if lst:
        return lst
    else:
        return None
    
def getcalculatenetsal(eid):
    v = empdetails.get(eid,-1)
    if v != -1:
        return v.cal_sal()
    else:
        return -1
    

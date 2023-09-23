import sqlite3 

try:
    conn = sqlite3.connect('database2.db')
    print("Connection Sucessfull....")
except:
    print("Connection failed....")
    
cursor = conn.cursor()

def addEmp():
    try:
        eid = int(input("Enter Employee Id : "))
        name = input("Enter Employee Name : ")
        salary = float(input("Enter Salaty :  "))
        cursor.execute("insert into Employee values (?,?,?)",(eid,name,salary))
        conn.commit()
        print("New Entry Added Sucessfully...")
    except Exception as e:     
        print("Error Occured : ",e)
        
def DelEmp(eid):
    try:
        cursor.execute("delete from Employee where empid = ? ",(eid,))
        conn.commit()
        return True
    except Exception as e:     
        print("Error Occured : ",e)

def UpdateEmp():
    try:
        eid = int(input("Enter Employee Id : "))
        name = input("Enter Employee Name : ")
        salary = float(input("Enter Salaty :  "))
        cursor.execute("update Employee set empid = ? , name = ? , salary = ?  where empid ",(eid,name,salary))
        conn.commit()
        return True
    except Exception as e:     
        print("Error Occured : ",e)
        
def DisplayEmp():
    try:
        cursor.execute("select * from Employee")
        for row in cursor.fetchall():
            name = row[1].rjust(8," ")
            print(f'Eid : {row[0]} | Name : {name} | Salary : {row[2]}')
    except Exception as e:     
        print("Error Occured : ",e)

while True:
    choice = int(input("""
                   1.Add Employee
                   2.Delete Employee
                   3.Update Employee
                   4.Display all Employees
                   5.Exit
                   Enter :- """))
    
    match choice:
        case 1:
            addEmp() 
        case 2:
            eid = int(input("Enter Employee ID : "))
            status = DelEmp(eid)
            if status:
                print("Deleted Sucessfully")
            else:
                print("Someting Went Wrong")
            
        case 3:
            status = UpdateEmp()
            if status:
                print("Updated Sucessfully")
            else:
                print("Someting Went Wrong")
            
        case 4:
            DisplayEmp()
            
        case 5: 
            print("Exiting....")
            conn.close()
            break

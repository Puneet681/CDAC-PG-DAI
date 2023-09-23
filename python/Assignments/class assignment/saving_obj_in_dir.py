import sys
import OOPs_ankush_day_9 as c
from saving_obj_in_dir_module import *

choice = 0
while choice != 8:
    choice = int(input("""
          1.Add New Employee
          2.Delete The Employee By ID
          3.Modify Sal or Charges
          4.Display All
          5.Calculate Net Salary by ID
          6.Display Only Given Type of Employee
          7.Display All With SAl > Given Value
          8.Exit
          """))
    match choice:
        case 1:
            ch = int(input("1,Salaried 2.Contract"))
            addnewemployee(ch)
        case 2:
            eid = input("enter eid")
            status = deleteemp(eid)
            if status == 1:
                print("delete succesfully")
            elif status == 2:
                print("found but not deleted")
            elif status == 3 :
                print("not found")
                
        case 3:
            eid = input("enter eid")
            if eid.startswith("s"):
                s = float(input("enter sal"))
                modifydetails(eid,s)
            else:
                hr = float(input("enter hrs"))
                ch = float(input("enter charges"))
                modifydetails(eid,hr,ch)
                
        case 4:
            displayall()
        case 5 :
            eid = input("enter eid")
            netsal = getcalculatenetsal(eid)
            if netsal != -1:
                print(f"{eid} ,{netsal}")
        case 6:
            ch = int(input("1,Salaried 2.Contract"))
            lst = findByType(ch)
            if lst!= None:
                for i in lst:
                    print(i)
            else:
                print("not found")
        case 7:
            ch = int(input("1,Salaried 2.Contract"))
            lst = findBysalary(ch)
            if lst!= None:
                for i in lst:
                    print(i)
            else:
                print("not found")
        case 8:
            print("thank you for visiting")
            sys.exit()
            
                
                
            
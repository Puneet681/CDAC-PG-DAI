import sys
from day_10_modularizing_OPPs_hobby_fuction_module import *

while True:
    case = int(input('''
                     1. add Freinds Details
                     2. Display All Friend
                     3. Search by id
                     4. Search by name
                     5. Display all friend with a particular hobby
                     6. Exit
                     '''))
    
    match case:
        case 1 :
            add_stud()
        case 2 :
            v = disp_all()
        case 3:
            status = search_by_id()
            if status != None:
                print(status)
            else:
                print("return not found")
        case 4 :
            name = input("Enter Student Name : ")
            status = search_by_name(name)
            if status != None:
                print(status)
            else:
                print("not found")
            
        case 5:
            hobb = input("Enter hobby : ")
            status = Hobbies(hobb)
            if status != None:
                for i in status:
                    print(i)
            else:
                print("not found")
                
        case 6:
            sys.exit()
                
            
            
